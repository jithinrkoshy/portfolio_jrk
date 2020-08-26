
$(document).ready(function(){

   
        $('.link_content').hover(function() {
            // alert("hover");
            var element  = $(this).find(".row_link")[0]
          $(element).css('opacity', '1');
        }, function() {
          // on mouseout, reset the background colour
          var element  = $(this).find(".row_link")[0]
          $(element).css('opacity', '0');
        });


        $("#dhruma-btn").click(function(){


          $("#overview-dhruma").removeClass("div-hide");
        });

        $("#dhruma-close").click(function(){


          $("#overview-dhruma").addClass("div-hide");
        });

        $("#davinci-btn").click(function(){


          $("#overview-davinci").removeClass("div-hide");
        });

        $("#davinci-close").click(function(){


          $("#overview-davinci").addClass("div-hide");
        });

        if (performance.navigation.type == performance.navigation.TYPE_RELOAD) {
          var st = window.location.href;
          split_st = st.split("/");
          st_length  = split_st.length
          if(split_st[st_length-2]=="success" && split_st[st_length-3]=="contact"){
            window.location.href = "http://"+ window.location.hostname +":8000/home/portfolio/contact";
          }


          
        }
      



});

