var csrftoken = $.cookie('csrftoken');
var myApp = angular.module('whackthemole', [], function($interpolateProvider){
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});
myApp.controller('initialize',function($scope,$http){
	$scope.score=0;
	$scope.grid=createGrid();
	$scope.spot=moleRandom($scope.grid);
	function createGrid(){
		var grid={};
		grid.rows=[];
		for(var i=0;i<5;i++){
			var row={};
			row.spots=[]
			for(var j=0;j<5;j++){
				var spot={};
				spot.isCovered=false;
				spot.click=false;
				row.spots.push(spot);
			}
			grid.rows.push(row);
		}
		return grid;
	}
	function moleRandom(grid){
		var row=Math.round(Math.random()*4);
		var column=Math.round(Math.random()*4);
		var spot=grid.rows[row].spots[column];
		spot.isCovered=true;
	}
	function getSpot(grid,row,column){
		return grid.rows[row].spots[column];
	}
	$scope.clickedMouse=function(spot){
		spot.click=true;
		if(spot.isCovered && spot.click){
			$scope.score+=10;
		}
		else{
			$scope.score-=5;
		}
		console.log($scope.score);
		return spot;
	}
	$scope.releasedMouse=function(spot){
		if(spot.isCovered){
			spot.click=0;
			spot.isCovered=0;
			moleRandom($scope.grid);
		}
	}

	$scope.endGame=function(){
		alert('Your Score : '+$scope.score);
		var args = {'score':$scope.score,'csrfmiddlewaretoken':csrftoken};
		$.post('/save/',args);
		console.log(args);
		window.location='../accounts/profile';
	}
	setTimeout(function(){
		alert('Your Score : '+$scope.score);
		var args = {'score':$scope.score,'csrfmiddlewaretoken':csrftoken};
		$.post('/save/',args);
		console.log(args);
		window.location='../accounts/profile';
	},60000);
}
);
