<!DOCTYPE html>
<html lang="en" dir="ltr">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="Content-Script-Type" content="text/javascript">
<meta name="robots" content="noindex">
<meta name="referrer" content="origin-when-crossorigin">
<title>Export: ultimate_drive_thru - Adminer</title>
<link rel="stylesheet" type="text/css" href="adminer.php?file=default.css&amp;version=4.3.1&amp;driver=mysql">
<script type="text/javascript" src="adminer.php?file=functions.js&amp;version=4.3.1&amp;driver=mysql"></script>
<link rel="shortcut icon" type="image/x-icon" href="adminer.php?file=favicon.ico&amp;version=4.3.1&amp;driver=mysql">
<link rel="apple-touch-icon" href="adminer.php?file=favicon.ico&amp;version=4.3.1&amp;driver=mysql">

<body class="ltr nojs" onkeydown="bodyKeydown(event);" onclick="bodyClick(event);">
<script type="text/javascript">
document.body.className = document.body.className.replace(/ nojs/, ' js');
var offlineMessage = 'You are offline.';
</script>

<div id="help" class="jush-sql jsonly hidden" onmouseover="helpOpen = 1;" onmouseout="helpMouseout(this, event);"></div>

<div id="content">
<p id="breadcrumb"><a href="adminer.php">MySQL</a> &raquo; <a href='adminer.php?username=drive_thru_user' accesskey='1' title='Alt+Shift+1'>Server</a> &raquo; <a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru">ultimate_drive_thru</a> &raquo; Export
<h2>Export: ultimate_drive_thru</h2>
<div id='ajaxstatus' class='jsonly hidden'></div>

<form action="" method="post">
<table cellspacing="0">
<tr><th>Output<td><label><input type='radio' name='output' value='text' checked>open</label><label><input type='radio' name='output' value='file'>save</label><label><input type='radio' name='output' value='gz'>gzip</label>
<tr><th>Format<td><label><input type='radio' name='format' value='sql' checked>SQL</label><label><input type='radio' name='format' value='csv'>CSV,</label><label><input type='radio' name='format' value='csv;'>CSV;</label><label><input type='radio' name='format' value='tsv'>TSV</label>
<tr><th>Database<td><select name='db_style'><option><option>USE<option>DROP+CREATE<option selected>CREATE</select><label><input type='checkbox' name='routines' value='1' checked>Routines</label><label><input type='checkbox' name='events' value='1' checked>Events</label><tr><th>Tables<td><select name='table_style'><option><option selected>DROP+CREATE<option>CREATE</select><label><input type='checkbox' name='auto_increment' value='1'>Auto Increment</label><label><input type='checkbox' name='triggers' value='1' checked>Triggers</label><tr><th>Data<td><select name='data_style'><option><option>TRUNCATE+INSERT<option selected>INSERT<option>INSERT+UPDATE</select></table>
<p><input type="submit" value="Export">
<input type="hidden" name="token" value="416277:315049">

<table cellspacing="0">
<thead><tr><th style='text-align: left;'><label class='block'><input type='checkbox' id='check-tables' checked onclick='formCheck(this, /^tables\[/);'>Tables</label><th style='text-align: right;'><label class='block'>Data<input type='checkbox' id='check-data' checked onclick='formCheck(this, /^data\[/);'></label></thead>
<tr><td><label class='block'><input type='checkbox' name='tables[]' value='Menu' checked onclick="checkboxClick(event, this); formUncheck(&#039;check-tables&#039;);">Menu</label><td align='right'><label class='block'><span id='Rows-Menu'></span><input type='checkbox' name='data[]' value='Menu' checked onclick="checkboxClick(event, this); formUncheck(&#039;check-data&#039;);"></label>
<tr><td><label class='block'><input type='checkbox' name='tables[]' value='orders' checked onclick="checkboxClick(event, this); formUncheck(&#039;check-tables&#039;);">orders</label><td align='right'><label class='block'><span id='Rows-orders'></span><input type='checkbox' name='data[]' value='orders' checked onclick="checkboxClick(event, this); formUncheck(&#039;check-data&#039;);"></label>
<tr><td><label class='block'><input type='checkbox' name='tables[]' value='transactions' checked onclick="checkboxClick(event, this); formUncheck(&#039;check-tables&#039;);">transactions</label><td align='right'><label class='block'><span id='Rows-transactions'></span><input type='checkbox' name='data[]' value='transactions' checked onclick="checkboxClick(event, this); formUncheck(&#039;check-data&#039;);"></label>
<tr><td><label class='block'><input type='checkbox' name='tables[]' value='type' checked onclick="checkboxClick(event, this); formUncheck(&#039;check-tables&#039;);">type</label><td align='right'><label class='block'><span id='Rows-type'></span><input type='checkbox' name='data[]' value='type' checked onclick="checkboxClick(event, this); formUncheck(&#039;check-data&#039;);"></label>
<script type='text/javascript'>ajaxSetHtml('adminer.php?username=drive_thru_user&db=ultimate_drive_thru&script=db');</script>
</table>
</form>
</div>

<form action="" method="post">
<p class="logout">
<input type="submit" name="logout" value="Logout" id="logout">
<input type="hidden" name="token" value="416277:315049">
</p>
</form>
<div id="menu">
<h1>
<a href='https://www.adminer.org/' target='_blank' id='h1'>Adminer</a> <span class="version">4.3.1</span>
<a href="https://www.adminer.org/#download" target="_blank" id="version"></a>
</h1>
<script type="text/javascript" src="adminer.php?file=jush.js&amp;version=4.3.1&amp;driver=mysql"></script>
<script type="text/javascript">
var jushLinks = { sql: [ 'adminer.php?username=drive_thru_user&db=ultimate_drive_thru&table=$&', /\b(Menu|orders|transactions|type)\b/g ] };
jushLinks.bac = jushLinks.sql;
jushLinks.bra = jushLinks.sql;
jushLinks.sqlite_quo = jushLinks.sql;
jushLinks.mssql_bra = jushLinks.sql;
bodyLoad('5.5');
</script>
<form action="">
<p id="dbs">
<input type="hidden" name="username" value="drive_thru_user"><span title='database'>DB</span>: <select name='db' onmousedown='dbMouseDown(event, this);' onchange='dbChange(this);'><option value=""><option>information_schema<option selected>ultimate_drive_thru</select><input type='submit' value='Use' class='hidden'>
<input type="hidden" name="dump" value=""></p></form>
<p class='links'><a href='adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;sql='>SQL command</a>
<a href='adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;import='>Import</a>
<a href='adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;dump=' id='dump' class='active '>Export</a>
<a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;create=">Create table</a>
<ul id='tables' onmouseover='menuOver(this, event);' onmouseout='menuOut(this);'>
<li><a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;select=Menu" class='select'>select</a> <a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;table=Menu" class='structure' title='Show structure'>Menu</a>
<li><a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;select=orders" class='select'>select</a> <a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;table=orders" class='structure' title='Show structure'>orders</a>
<li><a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;select=transactions" class='select'>select</a> <a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;table=transactions" class='structure' title='Show structure'>transactions</a>
<li><a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;select=type" class='select'>select</a> <a href="adminer.php?username=drive_thru_user&amp;db=ultimate_drive_thru&amp;table=type" class='structure' title='Show structure'>type</a>
</ul>
</div>
<script type="text/javascript">setupSubmitHighlight(document);</script>
