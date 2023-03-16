<html>
<body>

<?php

header('Access-Control-Allow-Origin: *');
$text = $_GET['text'];
passthru(`echo "$text" | ./venv3.7/bin/python ./prediction.py`);

?>

</body>
</html>
