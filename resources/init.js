// set objects to be used in multiple functions
var markersArray = [];
var map = null;
var datajson = [];
var weather = 1;
var userLatLong = {lat: 51.90923, lng: 4.486283};
var mapcenter = {lat: 51.92442, lng: 4.47773};

// this function will be called when google maps is loaded
function initMap() 
{
	// load the google map
	map = new google.maps.Map(document.getElementById('map'), {
		center: mapcenter,
		zoom: 13,
		disableDefaultUI: true
	});
	
	// load the custom marker libraries to put the custom markers on the screen
	InitCustomMarker();
	InitCustomLocationMarker();
  
	// load the checkboxes
	LoadData();
	
	// load the user location marker
	LoadUserMarker();
	
	// set the event for closing the marker
	$(".contentDetails").hide();
	$(".exitContainer").click(HideMarkerInfo);
}

// this function loads the default data from python
function LoadData(){
	$.ajax("/cgi-bin/main.py", {
		format: "json"
	}).done(function(data) {
		datajson = JSON.parse(data);
		LoadCheckboxes();
		LoadMarkers();
	});
}	

// this function loads the checkboxes according to the data from python
function LoadCheckboxes()
{
	var data = datajson;
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
	var data = datajson;
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
				var marker = new CustomMarker(
					myLatlng, 
					map,
					dataitem
				);
				markersArray.push(marker);
			}
		}
	}
	
	// set the weather
	if(data.length > 0)
	{
		if(data[0].weather.toLowerCase().indexOf("clear") > -1)
		{
			$(".weatherContainer").html("<i class='fa fa-sun-o'></i>");
		}
		else
		{
			$(".weatherContainer").html("<i class='fa fa-cloud'></i>");
		}
	}
}

// this function shows the data for the current market
function ShowMarkerInfo(data){
	$(".contentDetailsImage").attr("src", "");
	if($("#map").hasClass("col-xs-10")){
		$("#map").removeClass("col-xs-10");
		$("#map").addClass("col-xs-8");
		$(".contentDetails").addClass("col-xs-2");
		$(".contentDetails").show();
		google.maps.event.trigger(map, 'resize')
	}
	
	// get the image of the location
	$(".contentDetailsImage").attr("src","https://maps.googleapis.com/maps/api/streetview?size=600x300&location="+data.lat+","+data.lng+"&fov=120&heading=235&pitch=10&key=AIzaSyCg219BZX5-sVkO5423wOAIwRF_OxW7F8E"); 

	// get the route of the location
	$(".contentDetailsRoute").html(data.directions);
}

function HideMarkerInfo(){
	$(".contentDetails").hide();
	$("#map").addClass("col-xs-10");
	$("#map").removeClass("col-xs-8");
	$(".contentDetails").removeClass("col-xs-2");
	google.maps.event.trigger(map, 'resize')
}

// this function clears all the markers from the screen except the users location
function ClearMarkers() 
{
	for (var i = 0; i < markersArray.length; i++ ) {
		markersArray[i].setMap(null);
	}
	markersArray = []
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