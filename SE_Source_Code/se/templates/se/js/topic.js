    $( document ).ready( function(){
        $('.post').on('click','.more',function () {
             $(this).siblings('.social_icons').css({"display": "block"});
             $(this).siblings('.comments').css({"display": "block"});
             $('<div class="make_comment"><img src="../images/avatar.jpg" id="avatar"><form class="reply_form"><input type="text" name="make_comment" placeholder="Add a comment"><button>comment</button></form></div>').insertAfter($(this).siblings('.social_icons'));
            $(this).siblings('.answer').css({"height" :"auto"});
            $(this).css({"display" :"none"});

        });

                $('.comments').on('click','.comment_more',function () {
             $(this).siblings('.social_icons').css({"display": "block"});
             $(this).siblings('.comments').css({"display": "block"});
            $(this).siblings('.comment').css({"height" :"auto"});
            $(this).css({"display" :"none"});

        });
                $('.social_icons').on('click','.reply',function () {
                 $('<div class="make_comment"><img src="../images/avatar.jpg" id="avatar"><form class="reply_form"><input type="text" name="make_comment" placeholder="Add a comment"><button>comment</button></form></div>').insertAfter($(this).parent());
        });

});
    

    var temp = 1;

    function reply(el){
        $('<div class="make_reply"><img src="../images/avatar.jpg" id="avatar"><form class="reply_form2"><input type="text" name="make_comment" placeholder="Add a comment"><button>comment</button></form></div>').insertAfter($(el).parent());
    }

    function forum1() {
    var x = document.getElementById("forum");
    var y = document.getElementById("music");
    var z = document.getElementById("allquest");
    if (z.style.display === "none") {
        z.style.display = "block";
        //y.style.display = "none";
        x.style.backgroundColor = "#ffffff";
        y.style.backgroundColor = "#f2f2f2";
        x.style.fontWeight = 'bold';
        y.style.fontWeight='normal';
    }
    else {
        z.style.display = "block";
        x.style.backgroundColor = "#ffffff";
        y.style.backgroundColor = "#f2f2f2";
        x.style.fontWeight = 'bold';
        y.style.fontWeight='normal';
    }
 
  }
  function music1() {
    var x = document.getElementById("forum");
    var y = document.getElementById("music");
    var z = document.getElementById("allquest");
    if (z.style.display === "block") {
        z.style.display = "none";
        //x.style.display = "none";
        y.style.backgroundColor = "#ffffff";
        x.style.backgroundColor = "#f2f2f2";
        y.style.fontWeight = 'bold';
        x.style.fontWeight='normal';
    }
    else {
        z.style.display = "none";
        y.style.backgroundColor = "#ffffff";
        x.style.backgroundColor = "#f2f2f2";
        y.style.fontWeight = 'bold';
        x.style.fontWeight='normal';s
    }
 
  }
      function question() {
    var x = document.getElementById("formque");
    var y = document.getElementById("formpoll");
    var z = document.getElementById("downline1");
    var m = document.getElementById("downline2");
    if (x.style.display === "none") {
        x.style.display = "block";
        y.style.display = "none"
        z.style.borderBottom = "1.5px solid #ff0d22"
        m.style.borderBottom = "0px"
    }
    else {
        x.style.display = "block"
        y.style.display = "none"
        z.style.borderBottom = "1.5px solid #ff0d22"
    }
 
  }
  function poll() {
    var x = document.getElementById("formque");
    var y = document.getElementById("formpoll");
    var z = document.getElementById("downline2");
    var m = document.getElementById("downline1");
    if (y.style.display === "none") {
        y.style.display = "block";
        x.style.display = "none"
        z.style.borderBottom = "1.5px solid #ff0d22"
        m.style.borderBottom = "0px"

    }
    else {
        y.style.display = "block";
        x.style.display = "none"
        z.style.borderBottom = "1.5px solid #ff0d22"
        m.style.borderBottom = "0px"
    }
 
  }

  function opt3close(){
    var x = document.getElementById("ch3opt");
    var y = document.getElementById("ch4opt");
    var z = document.getElementById("addopt")
    z.style.display = "block"
    if(temp == 1)
    {
        $("#ch4opt").remove();
        $("#options_close2").remove()
        temp = 2;
    }
    else{
        $("#ch3opt").remove();
        $("#options_close1").remove();
        temp = 3;
    }

  }

    function opt4close() {
        $("#ch4opt").remove();
        $("#options_close2").remove();
        temp = 2;
        var z = document.getElementById("addopt")
        z.style.display = "block"
  }


function addot() {
    var z = document.getElementById("addopt");
    if(temp == 2)
    {
        $("#options .before:last").before('<div class="before"><input type="text" name="choice 4" placeholder="Choice 4(optional)" id="ch4opt"><a id="options_close2" onclick="opt4close()">&#10006 </a></div>');
        z.style.display = "none";
        temp = 1;

    }
    if(temp == 3){
        $("#options .before:last").before('<div class="before"><input type="text" name="choice 3" placeholder="Choice 3(optional)" id="ch3opt"><a id="options_close1" onclick="opt3close()">&#10006 </a></div>');
        z.style.display = "block";
        temp = 2;
    }
  }



  function openNav() {
    document.getElementById("mySidenav").style.width = "350px";
    document.getElementById("main").style.marginRight = "350px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.1)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";
}
// Get the modal
var modal = document.getElementById('modal');
var askque = document.getElementById('askque');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == askque) {
        askque.style.display = "none";
    }
}