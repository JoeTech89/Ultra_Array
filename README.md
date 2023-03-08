# Ultra Array
## Created By: Rukus Framework
#### Version 0.2 3/7/2023


<!DOCTYPE html>
<html>
<head> </head>

<body>

<h4>Custom Python Variable Types with expanded functionality.</h4>
<h6>Please use only the UltraArray version. Depreciated versions may already have been removed.</h6>
<h6>NOTE: Tuple object implementation is not working as intended.</h6>
<hr>
<p>This Pakage module contains various objects, that are to be used as expanded variable types.<br>
A pro to useing this package is the expanded funtionality types will have, as well as a more readable presentation when useing the <i>print</i> function.<br>
  Types included:
     <li>Dictionary (dict)</li>
     <li>Array  (list)</li>
     <li>Tupple (tupple) Note: Implementation not working as intended</li>
     <li>Singleton </li>
</p>
<hr>

<h1>Setup</h1>
  <p>
    <blockquote> import UltraAray as Ultra</blockquote> <br>
    To import the package this way will greatly increase simplicity in implementation
  </p>
<hr>

<h2>Singleton</h2>
<p>
  <blockquote>class ObjectName(Ultra.Singleton)</blockquote>
  A Singleton will allow the object which inherites it be singular, and not instanced when called.
</p>
<hr>

<h2>Dicitonary</h2>
<h4>Basic implementation</h4>
<p>
  <blockquote>d=Ultra.Dictionary(a=0,b=1,c=2,d=3)</blockquote>
  This will create a dictionary as d with the values appended.<br>
  You can also create it in a way to name the dictionary. This will allow the name to be shown when printing the dictionary.
  <blockquote>d=Ultra.Dictionary(a=0,b=1,c=2,d=3).set('name','My Dictionary')</blockquote>
  Now when you print <i>d</i> it will show the name before the information stored within.<br>
  It also contains an <i>append</i> method, much like <i>list</i>. However if the 'key' to append is already avaliable it will add a numeric value to the end of the 'key' name.
  <blockquote>d.append(a=4)</blockquote>
  After this function the dictionary will appear as: <i>d[a=0,b=1,c=2,d=3,a1=4]</i>  
</p>
<hr>

<h2>Array</h2>
<h4>Basic implementation</h4>
<p>
  <blockquote>a=Ultra.Array(1,2,3,4)</blockquote>
  This will create an array with the values appended.<br>
  You can also create it with the ~.set('name','Array Name') and will act as other types in this package do.
</p>

<h2>Tupple</h2>
<h4>Basic implementation</h4>
<p>
  <blockquote>t=Ultra.Tupple(1,2,3,4)</blockquote>
  <h4>Please Note: Currently this object is not working correctly. It is suggested that you do not use it.</h4>
</p>
<hr>

</body>
</html> 
