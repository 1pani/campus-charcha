  function forum1() {
    var x = document.getElementById("forum");
    var y = document.getElementById("music");
    var z = document.getElementById("topics_related");
    if (z.style.display === "none") {
        z.style.display = "grid";
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
    var z = document.getElementById("topics_related");
    if (z.style.display === "grid") {
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
        x.style.fontWeight='normal';
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