function functionA(x, y) {
    return x ^ y;
}

function functionC(y) {
    var z = 0;
    for (var i = 8 - y; i < 8; i++) {
        z += Math.pow(2, i);
    }
    return z;
}

function functionD(x, y) {
    y = y % 8;
    z = functionC(y);
    a = (x & z) >> (8 - y);
    return ((a) + (x << y)) & 0x00ff;
}

function functionE(parameter, key) {
    x = "";
    for (var i = 0; i < parameter.length; i++) {
        c = parameter.charCodeAt(i);
        if (i != 0) {
            t = x.charCodeAt(i - 1) % 2;
            switch (t) {
                case 0:
                    cr = functionA(c, key.charCodeAt(i % key.length));
                    break;
                case 1:
                    cr = functionD(c, key.charCodeAt(i % key.length));
                    break;
            }
        } else {
            cr = functionA(c, key.charCodeAt(i % key.length));
        }
        x += String.fromCharCode(cr);
    }
    return x;
}

function functionF(parameter) {
    var passwordNumber = 0;
    for (var i = 0; i < parameter.length; i++) {
        passwordNumber += parameter["charCodeAt"](i)
    }

    if (passwordNumber == 8932) {
        if(parameter.includes("<html>")){
            console.log("|" + parameter + "|");
            return true;
        }
        else{
            return false;
        }
        //var messageDialog = window.open("", "", "\x77\x69\x64\x74\x68\x3d\x33\x30\x30\x2c\x68\x65\x69\x67\x68\x74\x3d\x32\x20\x30");
        //messageDialog.document.write(parameter)
    } else {
        return false;
    }
}

var payload = "\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\xe1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e\x63\x47";


function generate(chars, current){
    var inserter = current.length - 1;
    for(var i = current.length - 1; i > 0; i--){
        if(current[i] == chars[chars.length - 1]){
            --inserter;
        }
        else{
            break;
        }
    }
    //console.log('inserter: ' + inserter + " | " + current[inserter]);
    //console.log("Index to change: " + current + " | " + current[inserter] + " (" + inserter + "/" + (current.length - 1) + ")");
    var deletedChar = current[inserter];
    var newCurrent = current.slice(0, inserter);
    //console.log("new current: " + newCurrent + " | deleted: " + deletedChar);
    var newCharIndex = chars.indexOf(deletedChar) + 1;
    var newChar = chars[newCharIndex];
    if(newChar === undefined){
        console.log('Done: ' + newChar);
        return null;
    }
    newCurrent += newChar;

    if(newCurrent.length < current.length){
        newCurrent += chars[0].repeat(current.length - newCurrent.length);
    }

    //console.log("current: " + newCurrent);
    return newCurrent;
}

// Bruteforce settings
var chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
var length = 6;
var start = chars[0].repeat(length);
start = "MyP4sS";

var run = true;

var totalCombinations = Math.pow((chars.length - 1), 6);
var delimeter = Math.floor(totalCombinations / 1000);

var first = generate(chars, start);
var iterations = 1;/*
for(var i = 0; i < start.length - 1; i++){
    var num = chars.length - chars.indexOf(start[i]) - 1;
    iterations *= num;
}*/
while(run){
    if(first === null){
        run = false;
        break;
    }

    var result = functionE(payload, first);
    if(result.includes("<html>")){
        console.log('Password: ' + first);
        break;
    }
    
    
    first = generate(chars, first);

    iterations++;
    if((iterations % delimeter) == 0){
        console.log(first);
        var percentCompletion = iterations / totalCombinations * 100;
        console.log("Progress: " + percentCompletion + "%");
    }
}