<!-- This line is all you need to enable HTML5 video and audio tags in all major browsers! -->
<!-- script type="text/javascript" src="/html/dist/api/1.2.2/html5media.min.js"></script> -->

<!-- This line enables all the other HTML5 elements in IE. It's not necessary if you just want to play video. -->
<!--[if lt IE 9]><script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7/html5shiv.min.js"></script><![endif]-->
<script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-24462944-1']);
      _gaq.push(['_trackPageview']);

      (function() {
          var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
          ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
          var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();
      function change_video(e){
          alert(e)
          var f = e.innerHTML;
          var v = document.getElementById("video");
          v.autoplay = "autoplay"
          v.src = "/html/dist/media/"+f;
      }
</script>
