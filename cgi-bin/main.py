#!/usr/local/bin/python

import markten
import locatie
import cgitb

# set the errors to visible
cgitb.enable(display=1)

# set the general settings
google_api_key = "AIzaSyCg219BZX5-sVkO5423wOAIwRF_OxW7F8E"
userlocation = [51.90923, 4.486283]
mapcenter = [51.92442, 4.47773]

# build the json string to use in html
pythondata = "["

# add the python data for the markets
pythondata = pythondata + "{name: 'Markten', data: ["
week = (1,1,1,1,1,1,1)      
marktadres = markten.GetMarkten(week)

# add the data for each individual market
for x in range(0,len(marktadres)):
	marktnaam = marktadres[x][1].replace("\xa0", "") # this is added in the CSV file for some reason
	marktlocatie = locatie.GetLatLong(marktnaam, google_api_key)
	marktafstand = locatie.GetDistanceMeters(userlocation[0], userlocation[1], marktlocatie[0], marktlocatie[1], google_api_key)
	pythondata = pythondata + "{ name: '"+str(marktnaam)+"', dist: '"+str(marktafstand)+"', walk: 300, transport: 100, lat: "+str(marktlocatie[0])+", lng: "+str(marktlocatie[1]) + " },"

pythondata = pythondata[:-1]
pythondata = pythondata + "]}"
pythondata = pythondata + "];";

# print the html to the screen
print "Content-type: text/html\r\n\r\n",
print """
<html>
<head>
	<!-- SCRIPT -->
	<script src="../resources/jquery.js"></script>
	<script src="../resources/jquery-migrate.js"></script>
	<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCg219BZX5-sVkO5423wOAIwRF_OxW7F8E&callback=initMap" defer></script>
	<script src="../resources/custommarker.js"></script>

	<!-- STYLE -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
	<link rel="stylesheet" href="../resources/style.css">

	<!-- DATA FROM PYTHON -->
	<script>
		var data = """ + pythondata + """
		var weather = 1;
		var userLatLong = {lat: """ + str(userlocation[0]) + """, lng: """ + str(userlocation[1]) + """};
		var mapcenter = {lat: """ + str(mapcenter[0]) + """, lng: """ + str(mapcenter[1]) + """};
	</script>
</head>
<body>
	<!-- CONTENT -->
	<div class="container-fluid">
		<div class="row">
			<div class="col-xs-12 header">
				<img src="../resources/walkornot.png" class="headerimage"/>
			</div>
		</div>
		<div class="row fullheightBig">
			<div class="col-sm-12 col-md-2 contentLeft">
				<h4>
					<b>Locaties</b>
				</h4>
				<div class="locationContainer"></div> 
			</div>
			<div id="map" class="col-sm-12 col-md-10 contentRight fullheightSmall">
			</div>
		</div>
	</div>

	<!-- JAVASCRIPT -->
	<script>
		// set objects to be used in multiple functions
		var markersArray = [];
		var map = null;

		// this function will be called when google maps is loaded
		function initMap() 
		{
			// load the google map
			map = new google.maps.Map(document.getElementById('map'), {
				center: mapcenter,
				zoom: 13
			});
			
			// load the custom marker libraries to put the custom markers on the screen
			InitCustomMarker();
			InitCustomLocationMarker();
		  
			// load the checkboxes
			LoadCheckboxes();
		  
			// load the individual markers
			LoadMarkers();
			
			// load the user location marker
			LoadUserMarker();
		}
		
		// this function loads the checkboxes according to the data from python
		function LoadCheckboxes()
		{
			$(".locationContainer").html("");
			for(var i = 0; i < data.length; i ++)
			{
				$(".locationContainer").append("<input type='checkbox' class='"+data[i].name+"-checkbox itemCheckbox' /><label>"+data[i].name+"</label>");
			}
			$(".itemCheckbox").click(LoadMarkers);
		}

		// this function loads the markers according to the data from python and the selected checkboxes
		function LoadMarkers()
		{
			ClearMarkers();
			for(var i = 0; i < data.length; i ++)
			{	
				var isCheckBoxChecked = $("."+data[i].name + "-checkbox").is(':checked');
				if(isCheckBoxChecked)
				{
					for(var p = 0; p < data[i].data.length; p++)
					{
						var dataitem = data[i].data[p];
						var myLatlng = new google.maps.LatLng(dataitem.lat, dataitem.lng);
						markersArray.push(new CustomMarker(
							myLatlng, 
							map,
							dataitem
						));
					}
				}
			}
		}

		// this function clears all the markers from the screen except the users location
		function ClearMarkers() 
		{
			for (var i = 0; i < markersArray.length; i++ ) {
				markersArray[i].setMap(null);
			}
			markersArray.length = 0;
		}

		// this function loads the user location marker on the screen
		function LoadUserMarker()
		{
			var myLatlng = new google.maps.LatLng(userLatLong.lat, userLatLong.lng);
			new CustomLocationMarker(
				myLatlng, 
				map,
				{}
			);
		}
	</script>
</body>
</html>
"""