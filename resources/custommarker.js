function CustomLocationMarker(latlng, map, args) {
	this.latlng = latlng;	
	this.args = args;	
	this.setMap(map);	
}

function InitCustomLocationMarker(){
	CustomLocationMarker.prototype = new google.maps.OverlayView();
	CustomLocationMarker.prototype.draw = function() {
		
		var self = this;
		if (!this.drawn) 
		{
			this.div = $("<div class='markerLocationContainer'><i class='fa fa-male fa-3x'></i></div>");
			this.drawn = true;
			var panes = this.getPanes();
			$(panes.overlayImage).append(this.div);
		}
		
		var point = this.getProjection().fromLatLngToDivPixel(this.latlng);
		if (point) {
			$(this.div).css('left',(point.x - 10) + 'px');
			$(this.div).css('top', (point.y - 20) + 'px');
		}
	};

	CustomLocationMarker.prototype.remove = function() {
		$(this.div).remove();
	};

	CustomLocationMarker.prototype.getPosition = function() {
		return this.latlng;	
	};
}

function CustomMarker(latlng, map, args) {
	this.latlng = latlng;	
	this.args = args;	
	this.setMap(map);	
}

function InitCustomMarker(){
	CustomMarker.prototype = new google.maps.OverlayView();
	CustomMarker.prototype.draw = function() {
		
		var self = this;

		if (!this.drawn) 
		{
			var weatherIcon = weather == 1 ? "<i class='fa fa-cloud'></i>" : "<i class='fa fa-sun-o'></i>"
		
			var walkOrNot = this.args.walk < this.args.transport;
			var walkColor = walkOrNot ? "#328432" : "#CC0000";
			var transportColor = !walkOrNot ? "#328432" : "#CC0000";
		
			this.div = $("<div class='markerContainer'>" +
						"<div class='markerDistanceContainer'><b>"+this.args.dist+"</b></div>" +
						"<div class='markerWeatherContainer'>"+weatherIcon+"</div>" +
						"<div class='markerWalkContainer' style='background-color: "+walkColor+"'><i class='fa fa-male'></i></div>" +
						"<div class='markerCarContainer' style='background-color: "+transportColor+"'><i class='fa fa-car'></i></div>" +
					"</div>");
			this.drawn = true;
			
			var panes = this.getPanes();
			$(panes.overlayImage).append(this.div);
		}
		
		var point = this.getProjection().fromLatLngToDivPixel(this.latlng);
		
		if (point) {
			$(this.div).css('left',(point.x - 10) + 'px');
			$(this.div).css('top', (point.y - 20) + 'px');
		}
	};

	CustomMarker.prototype.remove = function() {
		$(this.div).remove();
	};

	CustomMarker.prototype.getPosition = function() {
		return this.latlng;	
	};
}