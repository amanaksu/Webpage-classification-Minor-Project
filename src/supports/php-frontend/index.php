<form method='post' action='insert.php'>
<?php
	if(!empty($_GET["message"]))
		print $_GET["message"]."\nNumber of entries : ".$_GET["count"];
?>
<table>
	<tr>
		<td>
			URL:
		</td>
		<td>
			<input type='text' name='url' required=''/>
		</td>
	</tr>
	<tr>
		<td>
			Category:
		</td>
		<td>
			<select name='category'>
			<?php
				if(!empty($_GET["category"]))
				{
					print "<option>".$_GET["category"]."</option>";
				}
			?>
				<option>Arts</option>
				<option>Business</option>
				<option>Computers</option>
				<option>Games</option>
				<option>Health</option>
				<option>Home</option>
				<option>Kids and Teens</option>
				<option>News</option>
				<option>Recreation</option>
				<option>Reference</option>
				<option>Regional</option>
				<option>Science</option>
				<option>Shopping</option>
				<option>Society</option>
				<option>Sports</option>
			</select>
		</td>
	</tr>
	<tr>
		<td>
			<input type='submit' value='Submit'/>
		</td>
	</tr>
	
</table>
</form>

