

function loading(){

   var i=0;
  function myLoop(){

  
    setTimeout(function() {   //  call a 3s setTimeout when the loop is called
        w = (i+1).toString();
        w = w+"%";
        $("#percentage-text").text(w);
        $(".load-fragment").width(w);  //  your code here
        i++;                    //  increment the counter
        if (i < 100) {           //  if the counter < 10, call the loop function
          myLoop();             //  ..  again which will trigger another 
        }                       //  ..  setTimeout()
      }, 50);

    }
    myLoop();

    
    setTimeout(function(){

        window.location.href =   window.location.href + "home";
    
      },5500);
}

$(document).ready(function(){







  var direction = "";
  oldx = 0;

  $(document).mousemove(function(e){

    var el = $(".bg-p-container");


  if(e.pageY > oldx){
    console.log("down")
    el.css({ '-moz-transform': 'rotate3d(1, 0, 0,' + 70 + 'deg)'});
    
    
  }
  else{
    console.log("up")
    el.css({ '-moz-transform': 'rotate3d(1, 0, 0,' + 45 + 'deg)'});
  }

  oldx = e.pageY;

  });


  


});