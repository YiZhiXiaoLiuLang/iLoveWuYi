from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import os
import random
import urllib
import threading
import time
token={
    "114514":"C:/ki9dwzq7.txt",
    }
tokentime={"114514":1669999999
           }
Fatherpath = 'G:\小天才大杂烩\大的'#行末不能有斜杠（如C:/yzxll/Desktop/文件夹，不是C:/yzxll/Desktop/文件夹/）！

def fadmin(path):
    print("fadmin:收到path转义",path)
    if(path=="/admin"):
        return "admin主"
    return "无对应项！"
    
    
def teacher(path):
    path=urllib.parse.unquote(path)
    name=path.split("?")[-1]
    print(name)
    rc="""<!DOCTYPE html>
    <html>
    <meta charset="GBK">
    <title>我爱伍屹文件站|教程</title>
    <script src="js/jquery.min.js" type="text/javascript"></script>
    <script src="js/yzxll.js" type="text/javascript"></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
    #yuanjiao{ 
    font: color:#0FF;
    display: inline-block;
            width: 234px; 
            height:auto; 
    }
    #yuanjiao:hover{
                box-shadow: 0 10px 20px rgba(0,0,0,0.5);
                transform: translateY(-20px);
            }
            
    a.gv { 

            text-decoration:none; 
            background:url(img/but.png) repeat 0px 0px; 
            width: 130px; 
            height: 43px; 
            display: block; 
            text-align:center;		
            line-height:43px; 
            cursor:pointer;
            float:left;
            margin:8px 2px 8px 2px;
            font:18px/43px 'microsoft yahei'; color:#0FF;
            }
    a.gv:hover { 
            background: url(img/but.png) repeat 0px -43px; 
            color:#1d7eb8;
            -webkit-box-shadow: 0 0 6px #1d7eb8;
            transition-duration: 0.5s;
            }
    canvas {
        display: block;
        margin: 2em;
    }
    .bg-canvas {
        position: fixed;
        top: 0;
        left: 0;
        z-index: -1;
        width: 100%;
        height: 100%;
        margin: 0;
    }
    body {
        background-image: -webkit-linear-gradient(bottom, #d7dde6 40%, #97a8c0 80%);
        background-image: linear-gradient(to top, #d7dde6 40%, #97a8c0 80%);
        text-align:center;
        width: auto;
        height: 1000vh;
    }
    .footer {
    position: fixed;
    left: 10px;
    bottom: 5px;
    right: 10px; 
    width: 95%;
    color: black;
    text-align: center;
    }
    </style> 
    <body>


<div id="content" style="/* float:left; */text-align:left;"></div>

<script>
    $.get('%md_name%', function(response, status, xhr){
        $("#content").html(marked.parse(response));
    });
</script>

    <div class="footer">
    @Copyright 我爱伍屹文件站 开发：一只小流浪(qq3035969948) 运维：伍屹(qq1050661298) 项目地址:<a href="https://github.com/YiZhiXiaoLiuLang/iLoveWuYi">github</a>本站与我爱微软（杨岔路）无任何关系！！！！！！！ 2023 All Right Reserved. 
    <a href="https://beian.miit.gov.cn/" target="_blank" >嘤ICP备114514号</a>
    </div>
    <script>
    (function() {
        var W = window,
            D = document,
            R = D.documentElement,
            B = D.body,
            watchScroll = false,
            WSCROLL = {
                x: 0,
                y: 0
            },
            noop = function() {};

        // Check for canvas support, exit out if no supprt
        if (!W.CanvasRenderingContext2D) {
            return function() {
                return false;
            };
        }

        // Use Init function to keep users from having to use `new Canvallax`. Also keeps Canvallax prototype clean for util functions.
        function Canvallax(options) {
            return new Init(options);
        }

        // Only one scroll tracker that works for every Canvallax instance
        function onScroll() {
            WSCROLL.x = R.scrollLeft || B.scrollLeft;
            WSCROLL.y = R.scrollTop || B.scrollTop;
        }

        function Init(options) {

            var C = this;

            if (!watchScroll) {
                watchScroll = true;
                onScroll();
                W.addEventListener('scroll', onScroll);
            }

            if (options) {
                Canvallax.extend(this, options);
            }

            C.canvas = D.createElement('canvas');
            C.canvas.className = 'canvallax ' + C.className;
            C.parent.insertBefore(C.canvas, C.parent.firstChild);

            if (C.fullscreen) {
                C.resizeFullscreen();
                W.addEventListener('resize', C.resizeFullscreen.bind(C));
            } else {
                C.canvas.width = C.width;
                C.canvas.height = C.height;
            }

            C.ctx = C.canvas.getContext('2d');
            C.x = (options.x !== undefined ? options.x : WSCROLL.x);
            C.y = (options.y !== undefined ? options.y : WSCROLL.y);

            C.addElements(C.elements);
            C.damping = (!C.damping || C.damping < 1 ? 1 : C.damping);

            if (C.animating) {
                C.render();
            }

            return C;
        }


        ////////////////////////////////////////


        function zIndexSort(a, b) {
            return (a.zIndex === b.zIndex ? 0 : a.zIndex < b.zIndex ? -1 : 1);
        }

        function stop() {
            this.animating = false;
            return this;
        }

        Init.prototype = {
            scroll: true,
            parent: B,
            animating: true,
            elements: [],
            damping: 1,
            _x: 0,
            _y: 0,
            fullscreen: true,
            render: function() {
                var C = this,
                    i = 0,
                    len = C.elements.length,
                    el, distance;

                C.now = Date.now();

                if (C.animating !== false) {
                    requestAnimationFrame(C.render.bind(C));
                }

                if (C.scroll) {
                    C.x = (C.scroll === 'invert' || C.scroll === 'invertx' ? -WSCROLL.x : WSCROLL.x);
                    C.y = (C.scroll === 'invert' || C.scroll === 'inverty' ? -WSCROLL.y : WSCROLL.y);
                }

                C._x += (-C.x - C._x) / C.damping;
                C._y += (-C.y - C._y) / C.damping;

                C.ctx.clearRect(0, 0, C.canvas.width, C.canvas.height);

                for (; i < len; i++) {
                    C.ctx.save();
                    C.elements[i]._render(C.ctx, C);
                    C.ctx.restore();
                }
                return this;
            },

            resizeFullscreen: function() {
                this.canvas.width = W.innerWidth;
                this.canvas.height = W.innerHeight;
                return this;
            },

            addElement: function(element) {
                this.elements.push(element);
                this.elements.sort(zIndexSort);
                return this;
            },

            addElements: function(elements) {
                var i = 0,
                    len = elements.length;
                for (; i < len; i++) {
                    this.addElement(elements[i]);
                }
                return this;
            },

            play: function() {
                this.animation = true;
                this.render();
                return this;
            },

            stop: stop,
            pause: stop
        };


        ////////////////////////////////////////

        Canvallax.extend = function(target) {
            target = target || {};

            var length = arguments.length,
                i = 1;

            if (arguments.length === 1) {
                target = this;
                i = 0;
            }

            for (; i < length; i++) {
                if (!arguments[i]) {
                    continue;
                }
                for (var key in arguments[i]) {
                    if (arguments[i].hasOwnProperty(key)) {
                        target[key] = arguments[i][key];
                    }
                }
            }

            return target;
        };

        var elementPrototype = {
            x: 0,
            y: 0,
            opacity: 1,
            distance: 1,
            scale: true,

            render: noop,
            init: noop,

            _render: function(ctx, C) {
                var el = this,
                    distance = el.distance || 1;

                C.ctx.globalAlpha = el.opacity || 1;

                if (el.scale) {
                    C.ctx.scale(distance, distance);
                    C.ctx.translate(C._x, C._y);
                } else {
                    C.ctx.translate(C._x * distance, C._y * distance);
                }

                if (el.render) {
                    el.render.call(el, ctx, C);
                }
            }

        };

        Canvallax.createElement = function(defaults) {

            function elInit(options) {
                Canvallax.extend(this, options);
                this.init.apply(this, arguments);
            }

            function el(options) {
                return new elInit(options);
            }

            elInit.prototype = Canvallax.extend({}, elementPrototype, defaults);
            elInit.prototype.constructor = el;
            return el;
        }

        ////////////////////////////////////////

        Canvallax.Element = Canvallax.createElement();

        ////////////////////////////////////////

        Canvallax.Image = Canvallax.createElement({
            init: function(options) {

                if (options.nodeType === 1) {
                    this.image = options;
                } else if ((!this.image && options.src) || (typeof options === typeof "")) {
                    this.image = new Image();
                    this.image.src = options.src || options;
                }

            },
            render: function(ctx) {

                if (this.image) {
                    var drawArgs = [this.image];

                    if (this.crop) {
                        drawArgs.push(this.crop.x, this.crop.y, this.crop.width, this.crop.height);
                        this.width = (this.width ? this.width : this.crop.width);
                        this.height = (this.height ? this.height : this.crop.height);
                    }

                    drawArgs.push(this.x, this.y);

                    if (this.width && this.height) {
                        drawArgs.push(this.width, this.height);
                    }

                    ctx.drawImage.apply(ctx, drawArgs);
                }
            }
        });

        ////////////////////////////////////////

        return W.Canvallax = Canvallax;

    })();


    var can = Canvallax({
        className: 'bg-canvas',
        scroll: true, // (boolean|'invert'|'invertx'|'inverty') If true, the X and Y of the scene are tied to document's scroll for a typical parallax experience. Set to false if you want to control the scene's X and Y manually.
        x: 0, // Starting x. If tied to scroll, this will be overridden on render.
        y: 0, // Starting y. If tied to scroll, this will be overridden on render.
        damping: 40 // the 'easing' of the x & y position when updated. 1 = none, higher is longer. If you're syncing parallax items to regular items in the scroll, then you'll probably want a low damping.
    });
    /*
      // The canvallax instance can be animated with GSAP, not scroll, if you want!
      TweenMax.to(can,4,{
        //x: 1000,
        y: 1000,
        yoyo: true,
        ease: Cubic.easeInOut,
        repeat: -1,
      });
    */


    // Clouds
    (function() {

        ////////////////////////////////////////


        var origWidth = width = document.body.clientWidth,
            origHeight = height = document.body.clientHeight;

        var gradient = Canvallax.Element({
            width: width * 1.5,
            height: height * 1.1,
            zIndex: 1,
            pattern: (function() {
                var canvas = document.createElement('canvas'),
                    ctx = canvas.getContext('2d'),
                    gradient = ctx.createLinearGradient(0, 0, 0, height);
                gradient.addColorStop(0, '#07588A');
                gradient.addColorStop(1, '#E1F6F4');
                return gradient;
            })(),
            render: function(ctx) {
                ctx.fillStyle = this.pattern;
                ctx.fillRect(this.x, this.y, this.width, this.height);
            }
        });

        can.addElement(gradient);


        window.addEventListener('resize', function() {

            height = document.body.clientHeight;

            var i = can.elements.length,
                max = document.body.clientWidth,
                heightScale = height / origHeight;

            console.log(height, origHeight, heightScale);

            while (i--) {
                can.elements[i].maxX = max; //document.body.clientWidth;
                can.elements[i].origY = can.elements[i].origY || can.elements[i].y;
                can.elements[i].y = can.elements[i].origY * heightScale;
            }
        });

        ////////////////////////////////////////

        // Adapted from http://bost.ocks.org/mike/algorithms/
        function bestCandidateSampler(width, height, numCandidates) {

            var samples = [];

            function findDistance(a, b) {
                var dx = a[0] - b[0],
                    dy = a[1] - b[1];
                return dx * dx + dy * dy;
            }

            function findClosest(c) {
                var i = samples.length,
                    sample,
                    closest,
                    distance,
                    closestDistance;

                while (i--) {
                    sample = samples[i];
                    distance = findDistance(sample, c);

                    if (!closestDistance || distance < closestDistance) {
                        closest = sample;
                        closestDistance = distance;
                    }
                }

                return closest;
            }

            function getSample() {
                var bestCandidate,
                    bestDistance = 0,
                    i = 0,
                    c, d;

                c = [Math.random() * width, Math.random() * height];

                if (samples.length < 1) {
                    bestCandidate = c;
                } else {
                    for (; i < numCandidates; i++) {
                        c = [Math.random() * width, Math.random() * height];
                        d = findDistance(findClosest(c), c);

                        if (d > bestDistance) {
                            bestDistance = d;
                            bestCandidate = c;
                        }
                    }
                }

                samples.push(bestCandidate);
                //console.log('bestCandidate',bestCandidate);
                return bestCandidate;
            }

            getSample.all = function() {
                return samples;
            };
            getSample.samples = samples;

            return getSample;
        }

        var getCandidate = bestCandidateSampler(width, height, 10);

        var CLOUD_COUNT = 40,
            CLOUD_WIDTH = 510,
            CLOUD_HEIGHT = 260;

        CLOUD_COUNT = Math.floor((width * height) / (CLOUD_WIDTH * CLOUD_HEIGHT));

        var Cloud = Canvallax.createElement({

            init: function(options) {
                this.tex = {
                    x: 0,
                    y: options.texOffset || 0,
                    w: this.image.width,
                    h: this.image.height
                };
            },

            render: function(ctx) {
                //this.x = (this.x * this.distance) < this.maxX ? this.x + this.speed : -this.tex.w;
                this.x = (this.x * this.distance) > -this.tex.w ? this.x - this.speed : offsetDistance(this.maxX, this.distance); // / (this.distance || 1);

                ctx.drawImage(this.image, this.tex.x, this.tex.y, this.tex.w, this.tex.h, this.x, this.y, this.tex.w, this.tex.h);
            }

        });

        Cloud.prototype.maxX = width;
        Cloud.prototype.speed = 0.25;


        function offsetDistance(width, distance) {
            var d = (width / distance) / (2 - distance);
            return d;
        }

        function randomRange(min, max) {
            return Math.random() * (max - min) + min;
        }

        function randomizedCloud(image) {

            var canvas = document.createElement('canvas'),
                ctx = canvas.getContext('2d'),
                width = canvas.width = randomRange(400, 700), //CLOUD_WIDTH,
                height = canvas.height = randomRange(200, 260), //CLOUD_HEIGHT,
                w = image.width,
                h = image.height,
                halfw = w / 2,
                halfh = h / 2,
                i = Math.ceil(randomRange(20, 90)), //60
                flip,
                randScale,
                randTex,
                maxScale = 2.5,
                fullPi = Math.PI / 2;

            while (i--) {
                randScale = randomRange(0.4, maxScale);
                ctx.globalAlpha = Math.random() - 0.2;
                ctx.translate(randomRange(halfw, width - (w * maxScale * 1.3)), randomRange(halfh, height - (h * maxScale)));
                ctx.scale(randScale, randomRange(randScale - 0.3, randScale));
                ctx.translate(halfw, halfh);
                ctx.rotate(randomRange(0, fullPi));
                ctx.drawImage(image, -halfw, -halfh); //, w, h, 0, 0, w, h);
                ctx.setTransform(1, 0, 0, 1, 0, 0);
            }


            //document.body.appendChild(canvas);

            //var img = document.createElement('img');
            //img.src = canvas.toDataURL();

            return canvas;
        }

        var cloudImg = new Image();
        cloudImg.addEventListener('load', function() {

            var i = CLOUD_COUNT, //Math.ceil(CLOUD_COUNT * 0.5),
                el, rand, pos, tex;

            while (i--) {
                rand = Math.round(randomRange(0.5, 1.1) * 10) / 10;
                pos = getCandidate();
                tex = randomizedCloud(cloudImg);

                cloud = new Cloud({
                    image: tex,
                    maxX: width,
                    zIndex: rand * 13,
                    x: pos[0],
                    y: pos[1],
                    opacity: (rand < 0.8 ? 0.8 : rand),
                    distance: rand,
                    speed: rand * randomRange(0.1, 0.3)
                });

                can.addElement(cloud);
            }

            can.render();
        });
        cloudImg.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEYAAABGCAMAAABG8BK2AAAAYFBMVEX///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8GYpHzAAAAIHRSTlMAAwcLDxIWGh8kKzI5QEhPVl9qc3uEi5Sdpa64wcrV4c6KdP8AAAOeSURBVHgBndQJkvM8DoNhS+nv/ieONBH8FIs1nb83ZLfF1wBFZ17vNMZ8fPz79/GY46Xre8F85kRzzhdk/A2TOpSARpF/g0mdaI8XZjg47leA32Jo3wbEooNE/SFGrPOAiPxC+xaDAxBTxQqFoW8wGGof89E4j8nQUceo621h/KY8GuXx4Mg10vRZlPd55JCEnXlIQX7cE8pNp8Dob4oY8LjZTny8QEMo2o2hSqT5YImxchVNbpgZ3oVR4xVUgOlGS5fFKCPSWDY4Yu1xIKyEEqLfE0UUKcoJ9MFVsAhnaOpEGW4gyxFyLitOeRhZO8NJur1hKpWWCV03oaG9yYcYXvD7UPbetVOMNwqlWH6/b7sp29G1Z5g6LFGaY9uYB2A6M7evtVco3U3M1CCopOlNY8Q7cdZahxIMTpv7meR2NghWDqdu8MTZzwMqN+RaBkmdUgf7wMfN1d1cNSAFMdhQ3tLXu2STuclylwYL5QYhsGyLz499bcgxK1F5SmumvaoRrIwSjYutaGbVZIgze6wegLO6i8MD2kJ1N1cYKAUXTLnRWxtnYrMONWRRD+EsA3utw4mnKxNCZRgplK5T05ycvaaZCmtAOEKl+p4ge70k06mcdrQoPgGpbY1EboNyY7/ZHVsfK1BLhBAdCA5MGd719b0gUOJmg9vc5hf3E+K2y1EQDnCjxoGs3t84WiA6zI253rVy6MRnSKNxJtQcRY3xL90MkN6DYGZHI3zBMaF1NcoUQ3Oll+9RBqHb1uIzSTmv9LtQOJbC7Ci/fRsivh0+sBrYwix3GKe8No5yHJTDaZqhqOp8KC6BdmXrFKFaXUUWk7uCLsRPbuAZrmsPjCANBKChIZj/97IBzSJq3pgpymiYRmnxMLG9YbinUGCk5rxbUhJDy/yH+C5U3wP1FQWDL5AtWpNQm0IRz/ys+psCTSKuCObTjY3KhLoCrbUY7ZgIqHRXrTSFHxwfFjcM1fWF8devtJPK2XtM6nAOpcrCXDlVR967qRi6XOY78NJsi95gcsJynMXF2k6gAFFhVFGLz0loz5u0HGoEGF6qOoVgC6cOB6iBb0Ixue66p+p8F+v17VkhUTqGXP6pVptC8JU07z0Ga5VqjmUpvBvuC8wpej4bJiXK+ZHnazfXyfUSipxPVJQvMTjppUKlFUVvv8PIVftrSIRD+Q6DQ7a47wzE9xjaYJk1Fty1v8CYauOLm+fv3Cikjv4lBqVCAP6n/gfZhdXQlm1mfwAAAABJRU5ErkJggg==';



        ////////////////////////////////////////
        // Full cloud texture image

        /*
        var texture = new Image(),
            CLOUD_SPRITE_DISTANCE = 300;

        texture.addEventListener('load', function() {

          //return false;

          var i = Math.ceil(CLOUD_COUNT * 0.5),
              cloud, rand, pos, tex;

          while(i--) {
            rand = Math.round(randomRange(0.3, 0.9) * 10) / 10;
            pos = getCandidate();
            tex = Math.floor(rand < 0.6 ? randomRange(4,6) : randomRange(0,3)) * CLOUD_SPRITE_DISTANCE;

            cloud = new Cloud({
              image: texture,
              tex: {
                x: 0,
                y: tex || 0,
                w: 510,
                h: 260
              },
              maxX: width,
              opacity: (rand < 0.8 ? 0.8 : rand ),
              x: pos[0] - randomRange(0,width * 0.25), //randomRange(-300,window.innerWidth),
              y: pos[1], //Math.ceil((1 - rand) * (CLOUD_SPRITE_COUNT + 1)) * CLOUD_SPRITE_DISTANCE, // Randomize the texture based on distance. Further away clouds are blurry.
              distance: rand, //Math.random()
              speed: rand * randomRange(0.025,0.2),
            });

            can.addElement(cloud);
          }

        });
        texture.src = 'http://i.imgur.com/48yRQIF.png';
        /**/


    })();
    </script> 

    </body>
    </html>""".replace("%md_name%","/teach/"+name)
    return rc
        
def AutoRemoveToken():
    while True:
        withrm=[]
        for i in tokentime:
            if(tokentime[i]<=time.time()):
                print("will delete",i)
                withrm.append(i)
        for i in withrm:
            print("Delete token:"+i)
            print("Delete time:",time.time(),"ytime",tokentime[i])
            del tokentime[i]
            del token[i]
        time.sleep(1)
def fileserver(path):
    fa="""<!DOCTYPE html>
    <html>
    <meta charset="GBK">
    <title>我爱伍屹文件站|文件服务</title>
    <script src="/js/jquery.min.js" type="text/javascript"></script>
    <script src="/js/yzxll.js" type="text/javascript"></script>
    <style>
    #yuanjiao{ 
    font: color:#0FF;
    display: inline-block;
            width: 234px; 
            height:auto; 
    }
    #yuanjiao:hover{
                box-shadow: 0 10px 20px rgba(0,0,0,0.5);
                transform: translateY(-20px);
            }
            
    a.gv { 

            text-decoration:none; 
            background:url(img/but.png) repeat 0px 0px; 
            width: 130px; 
            height: 43px; 
            display: block; 
            text-align:center;		
            line-height:43px; 
            cursor:pointer;
            float:left;
            margin:8px 2px 8px 2px;
            font:18px/43px 'microsoft yahei'; color:#0FF;
            }
    a.gv:hover { 
            background: url(img/but.png) repeat 0px -43px; 
            color:#1d7eb8;
            -webkit-box-shadow: 0 0 6px #1d7eb8;
            transition-duration: 0.5s;
            }
    canvas {
        display: block;
        margin: 2em;
    }
    .bg-canvas {
        position: fixed;
        top: 0;
        left: 0;
        z-index: -1;
        width: 100%;
        height: 100%;
        margin: 0;
    }
    body {
        background-image: -webkit-linear-gradient(bottom, #d7dde6 40%, #97a8c0 80%);
        background-image: linear-gradient(to top, #d7dde6 40%, #97a8c0 80%);
        text-align:center;
        width: auto;
        height: 800vh;
    }
    .footer {
    position: fixed;
    left: 10px;
    bottom: 5px;
    right: 10px; 
    width: 95%;
    color: black;
    text-align: center;
    }
    </style> 
    <body>

    <h1 style="font:50px 'microsoft yahei'; color:#0FF;text-align:center;">我爱伍屹文件站 - 文件服务</h1> 
    <div>"""

    fb="""</div>

    <div class="footer">
    @Copyright 我爱伍屹文件站 开发：一只小流浪(qq3035969948) 运维：伍屹(qq1050661298) 项目地址:<a href="https://github.com/YiZhiXiaoLiuLang/iLoveWuYi">github</a>本站与我爱微软（杨岔路）无任何关系！！！！！！！ 2023 All Right Reserved. 
    <a href="https://beian.miit.gov.cn/" target="_blank" >嘤ICP备114514号</a>
    </div>
    <script>
    (function() {
        var W = window,
            D = document,
            R = D.documentElement,
            B = D.body,
            watchScroll = false,
            WSCROLL = {
                x: 0,
                y: 0
            },
            noop = function() {};

        // Check for canvas support, exit out if no supprt
        if (!W.CanvasRenderingContext2D) {
            return function() {
                return false;
            };
        }

        // Use Init function to keep users from having to use `new Canvallax`. Also keeps Canvallax prototype clean for util functions.
        function Canvallax(options) {
            return new Init(options);
        }

        // Only one scroll tracker that works for every Canvallax instance
        function onScroll() {
            WSCROLL.x = R.scrollLeft || B.scrollLeft;
            WSCROLL.y = R.scrollTop || B.scrollTop;
        }

        function Init(options) {

            var C = this;

            if (!watchScroll) {
                watchScroll = true;
                onScroll();
                W.addEventListener('scroll', onScroll);
            }

            if (options) {
                Canvallax.extend(this, options);
            }

            C.canvas = D.createElement('canvas');
            C.canvas.className = 'canvallax ' + C.className;
            C.parent.insertBefore(C.canvas, C.parent.firstChild);

            if (C.fullscreen) {
                C.resizeFullscreen();
                W.addEventListener('resize', C.resizeFullscreen.bind(C));
            } else {
                C.canvas.width = C.width;
                C.canvas.height = C.height;
            }

            C.ctx = C.canvas.getContext('2d');
            C.x = (options.x !== undefined ? options.x : WSCROLL.x);
            C.y = (options.y !== undefined ? options.y : WSCROLL.y);

            C.addElements(C.elements);
            C.damping = (!C.damping || C.damping < 1 ? 1 : C.damping);

            if (C.animating) {
                C.render();
            }

            return C;
        }


        ////////////////////////////////////////


        function zIndexSort(a, b) {
            return (a.zIndex === b.zIndex ? 0 : a.zIndex < b.zIndex ? -1 : 1);
        }

        function stop() {
            this.animating = false;
            return this;
        }

        Init.prototype = {
            scroll: true,
            parent: B,
            animating: true,
            elements: [],
            damping: 1,
            _x: 0,
            _y: 0,
            fullscreen: true,
            render: function() {
                var C = this,
                    i = 0,
                    len = C.elements.length,
                    el, distance;

                C.now = Date.now();

                if (C.animating !== false) {
                    requestAnimationFrame(C.render.bind(C));
                }

                if (C.scroll) {
                    C.x = (C.scroll === 'invert' || C.scroll === 'invertx' ? -WSCROLL.x : WSCROLL.x);
                    C.y = (C.scroll === 'invert' || C.scroll === 'inverty' ? -WSCROLL.y : WSCROLL.y);
                }

                C._x += (-C.x - C._x) / C.damping;
                C._y += (-C.y - C._y) / C.damping;

                C.ctx.clearRect(0, 0, C.canvas.width, C.canvas.height);

                for (; i < len; i++) {
                    C.ctx.save();
                    C.elements[i]._render(C.ctx, C);
                    C.ctx.restore();
                }
                return this;
            },

            resizeFullscreen: function() {
                this.canvas.width = W.innerWidth;
                this.canvas.height = W.innerHeight;
                return this;
            },

            addElement: function(element) {
                this.elements.push(element);
                this.elements.sort(zIndexSort);
                return this;
            },

            addElements: function(elements) {
                var i = 0,
                    len = elements.length;
                for (; i < len; i++) {
                    this.addElement(elements[i]);
                }
                return this;
            },

            play: function() {
                this.animation = true;
                this.render();
                return this;
            },

            stop: stop,
            pause: stop
        };


        ////////////////////////////////////////

        Canvallax.extend = function(target) {
            target = target || {};

            var length = arguments.length,
                i = 1;

            if (arguments.length === 1) {
                target = this;
                i = 0;
            }

            for (; i < length; i++) {
                if (!arguments[i]) {
                    continue;
                }
                for (var key in arguments[i]) {
                    if (arguments[i].hasOwnProperty(key)) {
                        target[key] = arguments[i][key];
                    }
                }
            }

            return target;
        };

        var elementPrototype = {
            x: 0,
            y: 0,
            opacity: 1,
            distance: 1,
            scale: true,

            render: noop,
            init: noop,

            _render: function(ctx, C) {
                var el = this,
                    distance = el.distance || 1;

                C.ctx.globalAlpha = el.opacity || 1;

                if (el.scale) {
                    C.ctx.scale(distance, distance);
                    C.ctx.translate(C._x, C._y);
                } else {
                    C.ctx.translate(C._x * distance, C._y * distance);
                }

                if (el.render) {
                    el.render.call(el, ctx, C);
                }
            }

        };

        Canvallax.createElement = function(defaults) {

            function elInit(options) {
                Canvallax.extend(this, options);
                this.init.apply(this, arguments);
            }

            function el(options) {
                return new elInit(options);
            }

            elInit.prototype = Canvallax.extend({}, elementPrototype, defaults);
            elInit.prototype.constructor = el;
            return el;
        }

        ////////////////////////////////////////

        Canvallax.Element = Canvallax.createElement();

        ////////////////////////////////////////

        Canvallax.Image = Canvallax.createElement({
            init: function(options) {

                if (options.nodeType === 1) {
                    this.image = options;
                } else if ((!this.image && options.src) || (typeof options === typeof "")) {
                    this.image = new Image();
                    this.image.src = options.src || options;
                }

            },
            render: function(ctx) {

                if (this.image) {
                    var drawArgs = [this.image];

                    if (this.crop) {
                        drawArgs.push(this.crop.x, this.crop.y, this.crop.width, this.crop.height);
                        this.width = (this.width ? this.width : this.crop.width);
                        this.height = (this.height ? this.height : this.crop.height);
                    }

                    drawArgs.push(this.x, this.y);

                    if (this.width && this.height) {
                        drawArgs.push(this.width, this.height);
                    }

                    ctx.drawImage.apply(ctx, drawArgs);
                }
            }
        });

        ////////////////////////////////////////

        return W.Canvallax = Canvallax;

    })();


    var can = Canvallax({
        className: 'bg-canvas',
        scroll: true, // (boolean|'invert'|'invertx'|'inverty') If true, the X and Y of the scene are tied to document's scroll for a typical parallax experience. Set to false if you want to control the scene's X and Y manually.
        x: 0, // Starting x. If tied to scroll, this will be overridden on render.
        y: 0, // Starting y. If tied to scroll, this will be overridden on render.
        damping: 40 // the 'easing' of the x & y position when updated. 1 = none, higher is longer. If you're syncing parallax items to regular items in the scroll, then you'll probably want a low damping.
    });
    /*
      // The canvallax instance can be animated with GSAP, not scroll, if you want!
      TweenMax.to(can,4,{
        //x: 1000,
        y: 1000,
        yoyo: true,
        ease: Cubic.easeInOut,
        repeat: -1,
      });
    */


    // Clouds
    (function() {

        ////////////////////////////////////////


        var origWidth = width = document.body.clientWidth,
            origHeight = height = document.body.clientHeight;

        var gradient = Canvallax.Element({
            width: width * 1.5,
            height: height * 1.1,
            zIndex: 1,
            pattern: (function() {
                var canvas = document.createElement('canvas'),
                    ctx = canvas.getContext('2d'),
                    gradient = ctx.createLinearGradient(0, 0, 0, height);
                gradient.addColorStop(0, '#07588A');
                gradient.addColorStop(1, '#E1F6F4');
                return gradient;
            })(),
            render: function(ctx) {
                ctx.fillStyle = this.pattern;
                ctx.fillRect(this.x, this.y, this.width, this.height);
            }
        });

        can.addElement(gradient);


        window.addEventListener('resize', function() {

            height = document.body.clientHeight;

            var i = can.elements.length,
                max = document.body.clientWidth,
                heightScale = height / origHeight;

            console.log(height, origHeight, heightScale);

            while (i--) {
                can.elements[i].maxX = max; //document.body.clientWidth;
                can.elements[i].origY = can.elements[i].origY || can.elements[i].y;
                can.elements[i].y = can.elements[i].origY * heightScale;
            }
        });

        ////////////////////////////////////////

        // Adapted from http://bost.ocks.org/mike/algorithms/
        function bestCandidateSampler(width, height, numCandidates) {

            var samples = [];

            function findDistance(a, b) {
                var dx = a[0] - b[0],
                    dy = a[1] - b[1];
                return dx * dx + dy * dy;
            }

            function findClosest(c) {
                var i = samples.length,
                    sample,
                    closest,
                    distance,
                    closestDistance;

                while (i--) {
                    sample = samples[i];
                    distance = findDistance(sample, c);

                    if (!closestDistance || distance < closestDistance) {
                        closest = sample;
                        closestDistance = distance;
                    }
                }

                return closest;
            }

            function getSample() {
                var bestCandidate,
                    bestDistance = 0,
                    i = 0,
                    c, d;

                c = [Math.random() * width, Math.random() * height];

                if (samples.length < 1) {
                    bestCandidate = c;
                } else {
                    for (; i < numCandidates; i++) {
                        c = [Math.random() * width, Math.random() * height];
                        d = findDistance(findClosest(c), c);

                        if (d > bestDistance) {
                            bestDistance = d;
                            bestCandidate = c;
                        }
                    }
                }

                samples.push(bestCandidate);
                //console.log('bestCandidate',bestCandidate);
                return bestCandidate;
            }

            getSample.all = function() {
                return samples;
            };
            getSample.samples = samples;

            return getSample;
        }

        var getCandidate = bestCandidateSampler(width, height, 10);

        var CLOUD_COUNT = 40,
            CLOUD_WIDTH = 510,
            CLOUD_HEIGHT = 260;

        CLOUD_COUNT = Math.floor((width * height) / (CLOUD_WIDTH * CLOUD_HEIGHT));

        var Cloud = Canvallax.createElement({

            init: function(options) {
                this.tex = {
                    x: 0,
                    y: options.texOffset || 0,
                    w: this.image.width,
                    h: this.image.height
                };
            },

            render: function(ctx) {
                //this.x = (this.x * this.distance) < this.maxX ? this.x + this.speed : -this.tex.w;
                this.x = (this.x * this.distance) > -this.tex.w ? this.x - this.speed : offsetDistance(this.maxX, this.distance); // / (this.distance || 1);

                ctx.drawImage(this.image, this.tex.x, this.tex.y, this.tex.w, this.tex.h, this.x, this.y, this.tex.w, this.tex.h);
            }

        });

        Cloud.prototype.maxX = width;
        Cloud.prototype.speed = 0.25;


        function offsetDistance(width, distance) {
            var d = (width / distance) / (2 - distance);
            return d;
        }

        function randomRange(min, max) {
            return Math.random() * (max - min) + min;
        }

        function randomizedCloud(image) {

            var canvas = document.createElement('canvas'),
                ctx = canvas.getContext('2d'),
                width = canvas.width = randomRange(400, 700), //CLOUD_WIDTH,
                height = canvas.height = randomRange(200, 260), //CLOUD_HEIGHT,
                w = image.width,
                h = image.height,
                halfw = w / 2,
                halfh = h / 2,
                i = Math.ceil(randomRange(20, 90)), //60
                flip,
                randScale,
                randTex,
                maxScale = 2.5,
                fullPi = Math.PI / 2;

            while (i--) {
                randScale = randomRange(0.4, maxScale);
                ctx.globalAlpha = Math.random() - 0.2;
                ctx.translate(randomRange(halfw, width - (w * maxScale * 1.3)), randomRange(halfh, height - (h * maxScale)));
                ctx.scale(randScale, randomRange(randScale - 0.3, randScale));
                ctx.translate(halfw, halfh);
                ctx.rotate(randomRange(0, fullPi));
                ctx.drawImage(image, -halfw, -halfh); //, w, h, 0, 0, w, h);
                ctx.setTransform(1, 0, 0, 1, 0, 0);
            }


            //document.body.appendChild(canvas);

            //var img = document.createElement('img');
            //img.src = canvas.toDataURL();

            return canvas;
        }

        var cloudImg = new Image();
        cloudImg.addEventListener('load', function() {

            var i = CLOUD_COUNT, //Math.ceil(CLOUD_COUNT * 0.5),
                el, rand, pos, tex;

            while (i--) {
                rand = Math.round(randomRange(0.5, 1.1) * 10) / 10;
                pos = getCandidate();
                tex = randomizedCloud(cloudImg);

                cloud = new Cloud({
                    image: tex,
                    maxX: width,
                    zIndex: rand * 13,
                    x: pos[0],
                    y: pos[1],
                    opacity: (rand < 0.8 ? 0.8 : rand),
                    distance: rand,
                    speed: rand * randomRange(0.1, 0.3)
                });

                can.addElement(cloud);
            }

            can.render();
        });
        cloudImg.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEYAAABGCAMAAABG8BK2AAAAYFBMVEX///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8GYpHzAAAAIHRSTlMAAwcLDxIWGh8kKzI5QEhPVl9qc3uEi5Sdpa64wcrV4c6KdP8AAAOeSURBVHgBndQJkvM8DoNhS+nv/ieONBH8FIs1nb83ZLfF1wBFZ17vNMZ8fPz79/GY46Xre8F85kRzzhdk/A2TOpSARpF/g0mdaI8XZjg47leA32Jo3wbEooNE/SFGrPOAiPxC+xaDAxBTxQqFoW8wGGof89E4j8nQUceo621h/KY8GuXx4Mg10vRZlPd55JCEnXlIQX7cE8pNp8Dob4oY8LjZTny8QEMo2o2hSqT5YImxchVNbpgZ3oVR4xVUgOlGS5fFKCPSWDY4Yu1xIKyEEqLfE0UUKcoJ9MFVsAhnaOpEGW4gyxFyLitOeRhZO8NJur1hKpWWCV03oaG9yYcYXvD7UPbetVOMNwqlWH6/b7sp29G1Z5g6LFGaY9uYB2A6M7evtVco3U3M1CCopOlNY8Q7cdZahxIMTpv7meR2NghWDqdu8MTZzwMqN+RaBkmdUgf7wMfN1d1cNSAFMdhQ3tLXu2STuclylwYL5QYhsGyLz499bcgxK1F5SmumvaoRrIwSjYutaGbVZIgze6wegLO6i8MD2kJ1N1cYKAUXTLnRWxtnYrMONWRRD+EsA3utw4mnKxNCZRgplK5T05ycvaaZCmtAOEKl+p4ge70k06mcdrQoPgGpbY1EboNyY7/ZHVsfK1BLhBAdCA5MGd719b0gUOJmg9vc5hf3E+K2y1EQDnCjxoGs3t84WiA6zI253rVy6MRnSKNxJtQcRY3xL90MkN6DYGZHI3zBMaF1NcoUQ3Oll+9RBqHb1uIzSTmv9LtQOJbC7Ci/fRsivh0+sBrYwix3GKe8No5yHJTDaZqhqOp8KC6BdmXrFKFaXUUWk7uCLsRPbuAZrmsPjCANBKChIZj/97IBzSJq3pgpymiYRmnxMLG9YbinUGCk5rxbUhJDy/yH+C5U3wP1FQWDL5AtWpNQm0IRz/ys+psCTSKuCObTjY3KhLoCrbUY7ZgIqHRXrTSFHxwfFjcM1fWF8devtJPK2XtM6nAOpcrCXDlVR967qRi6XOY78NJsi95gcsJynMXF2k6gAFFhVFGLz0loz5u0HGoEGF6qOoVgC6cOB6iBb0Ixue66p+p8F+v17VkhUTqGXP6pVptC8JU07z0Ga5VqjmUpvBvuC8wpej4bJiXK+ZHnazfXyfUSipxPVJQvMTjppUKlFUVvv8PIVftrSIRD+Q6DQ7a47wzE9xjaYJk1Fty1v8CYauOLm+fv3Cikjv4lBqVCAP6n/gfZhdXQlm1mfwAAAABJRU5ErkJggg==';



        ////////////////////////////////////////
        // Full cloud texture image

        /*
        var texture = new Image(),
            CLOUD_SPRITE_DISTANCE = 300;

        texture.addEventListener('load', function() {

          //return false;

          var i = Math.ceil(CLOUD_COUNT * 0.5),
              cloud, rand, pos, tex;

          while(i--) {
            rand = Math.round(randomRange(0.3, 0.9) * 10) / 10;
            pos = getCandidate();
            tex = Math.floor(rand < 0.6 ? randomRange(4,6) : randomRange(0,3)) * CLOUD_SPRITE_DISTANCE;

            cloud = new Cloud({
              image: texture,
              tex: {
                x: 0,
                y: tex || 0,
                w: 510,
                h: 260
              },
              maxX: width,
              opacity: (rand < 0.8 ? 0.8 : rand ),
              x: pos[0] - randomRange(0,width * 0.25), //randomRange(-300,window.innerWidth),
              y: pos[1], //Math.ceil((1 - rand) * (CLOUD_SPRITE_COUNT + 1)) * CLOUD_SPRITE_DISTANCE, // Randomize the texture based on distance. Further away clouds are blurry.
              distance: rand, //Math.random()
              speed: rand * randomRange(0.025,0.2),
            });

            can.addElement(cloud);
          }

        });
        texture.src = 'http://i.imgur.com/48yRQIF.png';
        /**/


    })();
    </script> 

    </body>
    </html>"""

    fc="""<div id="yuanjiao"><a href="我爱伍屹文件站 114514">
            <img src="/img/flogo.png" width="234" height="234">
            <p>我爱伍屹文件站 yyds</p></a>
            </div>"""
    path=urllib.parse.unquote(path)
    if(os.path.isfile(Fatherpath+path)):
        if(len(token)>64):
            print("token池子爆了")
            return """<!DOCTYPE html>
<html>
<meta charset="GBK">
<title>我爱伍屹文件站</title>
<script src="js/jquery.min.js" type="text/javascript"></script>
<script src="js/yzxll.js" type="text/javascript"></script>
<style>
a.gv { 

	text-decoration:none; 
	background:url(img/but.png) repeat 0px 0px; 
	width: 130px; 
	height: 43px; 
	display: block; 
	text-align:center;		
	line-height:43px; 
	cursor:pointer;
	float:left;
	margin:8px 2px 8px 2px;
	font:18px/43px 'microsoft yahei'; color:#0FF;
	}
a.gv:hover { 
	background: url(img/but.png) repeat 0px -43px; 
	color:#1d7eb8;
	-webkit-box-shadow: 0 0 6px #1d7eb8;
	transition-duration: 0.5s;
	}
canvas {
    display: block;
    margin: 2em;
}
.bg-canvas {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
    width: 100%;
    height: 100%;
    margin: 0;
}
body {
    background-image: -webkit-linear-gradient(bottom, #d7dde6 40%, #97a8c0 80%);
    background-image: linear-gradient(to top, #d7dde6 40%, #97a8c0 80%);
    text-align:center;
    width: auto;
    height: 100vh;
}
.footer {
position: fixed;
left: 10px;
bottom: 5px;
right: 10px; 
width: 95%;
color: black;
text-align: center;
}
</style> 
<body>

<h1 style="font:50px 'microsoft yahei'; color:#0FF;text-align:center;">我爱伍屹文件站</h1> 
<div style="padding: 0px 20%">
<h2>FileToken池已满！请10分钟后再试！</h2>
</div>
<div class="footer">
@Copyright 我爱伍屹文件站 开发：一只小流浪(qq3035969948) 运维：伍屹(qq1050661298) 项目地址:<a href="https://github.com/YiZhiXiaoLiuLang/iLoveWuYi">github</a>本站与我爱微软（杨岔路）无任何关系！！！！！！！ 2023 All Right Reserved. 
<a href="https://beian.miit.gov.cn/" target="_blank" >嘤ICP备114514号</a>
</div>
<script>
(function() {
    var W = window,
        D = document,
        R = D.documentElement,
        B = D.body,
        watchScroll = false,
        WSCROLL = {
            x: 0,
            y: 0
        },
        noop = function() {};

    // Check for canvas support, exit out if no supprt
    if (!W.CanvasRenderingContext2D) {
        return function() {
            return false;
        };
    }

    // Use Init function to keep users from having to use `new Canvallax`. Also keeps Canvallax prototype clean for util functions.
    function Canvallax(options) {
        return new Init(options);
    }

    // Only one scroll tracker that works for every Canvallax instance
    function onScroll() {
        WSCROLL.x = R.scrollLeft || B.scrollLeft;
        WSCROLL.y = R.scrollTop || B.scrollTop;
    }

    function Init(options) {

        var C = this;

        if (!watchScroll) {
            watchScroll = true;
            onScroll();
            W.addEventListener('scroll', onScroll);
        }

        if (options) {
            Canvallax.extend(this, options);
        }

        C.canvas = D.createElement('canvas');
        C.canvas.className = 'canvallax ' + C.className;
        C.parent.insertBefore(C.canvas, C.parent.firstChild);

        if (C.fullscreen) {
            C.resizeFullscreen();
            W.addEventListener('resize', C.resizeFullscreen.bind(C));
        } else {
            C.canvas.width = C.width;
            C.canvas.height = C.height;
        }

        C.ctx = C.canvas.getContext('2d');
        C.x = (options.x !== undefined ? options.x : WSCROLL.x);
        C.y = (options.y !== undefined ? options.y : WSCROLL.y);

        C.addElements(C.elements);
        C.damping = (!C.damping || C.damping < 1 ? 1 : C.damping);

        if (C.animating) {
            C.render();
        }

        return C;
    }


    ////////////////////////////////////////


    function zIndexSort(a, b) {
        return (a.zIndex === b.zIndex ? 0 : a.zIndex < b.zIndex ? -1 : 1);
    }

    function stop() {
        this.animating = false;
        return this;
    }

    Init.prototype = {
        scroll: true,
        parent: B,
        animating: true,
        elements: [],
        damping: 1,
        _x: 0,
        _y: 0,
        fullscreen: true,
        render: function() {
            var C = this,
                i = 0,
                len = C.elements.length,
                el, distance;

            C.now = Date.now();

            if (C.animating !== false) {
                requestAnimationFrame(C.render.bind(C));
            }

            if (C.scroll) {
                C.x = (C.scroll === 'invert' || C.scroll === 'invertx' ? -WSCROLL.x : WSCROLL.x);
                C.y = (C.scroll === 'invert' || C.scroll === 'inverty' ? -WSCROLL.y : WSCROLL.y);
            }

            C._x += (-C.x - C._x) / C.damping;
            C._y += (-C.y - C._y) / C.damping;

            C.ctx.clearRect(0, 0, C.canvas.width, C.canvas.height);

            for (; i < len; i++) {
                C.ctx.save();
                C.elements[i]._render(C.ctx, C);
                C.ctx.restore();
            }
            return this;
        },

        resizeFullscreen: function() {
            this.canvas.width = W.innerWidth;
            this.canvas.height = W.innerHeight;
            return this;
        },

        addElement: function(element) {
            this.elements.push(element);
            this.elements.sort(zIndexSort);
            return this;
        },

        addElements: function(elements) {
            var i = 0,
                len = elements.length;
            for (; i < len; i++) {
                this.addElement(elements[i]);
            }
            return this;
        },

        play: function() {
            this.animation = true;
            this.render();
            return this;
        },

        stop: stop,
        pause: stop
    };


    ////////////////////////////////////////

    Canvallax.extend = function(target) {
        target = target || {};

        var length = arguments.length,
            i = 1;

        if (arguments.length === 1) {
            target = this;
            i = 0;
        }

        for (; i < length; i++) {
            if (!arguments[i]) {
                continue;
            }
            for (var key in arguments[i]) {
                if (arguments[i].hasOwnProperty(key)) {
                    target[key] = arguments[i][key];
                }
            }
        }

        return target;
    };

    var elementPrototype = {
        x: 0,
        y: 0,
        opacity: 1,
        distance: 1,
        scale: true,

        render: noop,
        init: noop,

        _render: function(ctx, C) {
            var el = this,
                distance = el.distance || 1;

            C.ctx.globalAlpha = el.opacity || 1;

            if (el.scale) {
                C.ctx.scale(distance, distance);
                C.ctx.translate(C._x, C._y);
            } else {
                C.ctx.translate(C._x * distance, C._y * distance);
            }

            if (el.render) {
                el.render.call(el, ctx, C);
            }
        }

    };

    Canvallax.createElement = function(defaults) {

        function elInit(options) {
            Canvallax.extend(this, options);
            this.init.apply(this, arguments);
        }

        function el(options) {
            return new elInit(options);
        }

        elInit.prototype = Canvallax.extend({}, elementPrototype, defaults);
        elInit.prototype.constructor = el;
        return el;
    }

    ////////////////////////////////////////

    Canvallax.Element = Canvallax.createElement();

    ////////////////////////////////////////

    Canvallax.Image = Canvallax.createElement({
        init: function(options) {

            if (options.nodeType === 1) {
                this.image = options;
            } else if ((!this.image && options.src) || (typeof options === typeof "")) {
                this.image = new Image();
                this.image.src = options.src || options;
            }

        },
        render: function(ctx) {

            if (this.image) {
                var drawArgs = [this.image];

                if (this.crop) {
                    drawArgs.push(this.crop.x, this.crop.y, this.crop.width, this.crop.height);
                    this.width = (this.width ? this.width : this.crop.width);
                    this.height = (this.height ? this.height : this.crop.height);
                }

                drawArgs.push(this.x, this.y);

                if (this.width && this.height) {
                    drawArgs.push(this.width, this.height);
                }

                ctx.drawImage.apply(ctx, drawArgs);
            }
        }
    });

    ////////////////////////////////////////

    return W.Canvallax = Canvallax;

})();


var can = Canvallax({
    className: 'bg-canvas',
    scroll: true, // (boolean|'invert'|'invertx'|'inverty') If true, the X and Y of the scene are tied to document's scroll for a typical parallax experience. Set to false if you want to control the scene's X and Y manually.
    x: 0, // Starting x. If tied to scroll, this will be overridden on render.
    y: 0, // Starting y. If tied to scroll, this will be overridden on render.
    damping: 40 // the 'easing' of the x & y position when updated. 1 = none, higher is longer. If you're syncing parallax items to regular items in the scroll, then you'll probably want a low damping.
});
/*
  // The canvallax instance can be animated with GSAP, not scroll, if you want!
  TweenMax.to(can,4,{
    //x: 1000,
    y: 1000,
    yoyo: true,
    ease: Cubic.easeInOut,
    repeat: -1,
  });
*/


// Clouds
(function() {

    ////////////////////////////////////////


    var origWidth = width = document.body.clientWidth,
        origHeight = height = document.body.clientHeight;

    var gradient = Canvallax.Element({
        width: width * 1.5,
        height: height * 1.1,
        zIndex: 1,
        pattern: (function() {
            var canvas = document.createElement('canvas'),
                ctx = canvas.getContext('2d'),
                gradient = ctx.createLinearGradient(0, 0, 0, height);
            gradient.addColorStop(0, '#07588A');
            gradient.addColorStop(1, '#E1F6F4');
            return gradient;
        })(),
        render: function(ctx) {
            ctx.fillStyle = this.pattern;
            ctx.fillRect(this.x, this.y, this.width, this.height);
        }
    });

    can.addElement(gradient);


    window.addEventListener('resize', function() {

        height = document.body.clientHeight;

        var i = can.elements.length,
            max = document.body.clientWidth,
            heightScale = height / origHeight;

        console.log(height, origHeight, heightScale);

        while (i--) {
            can.elements[i].maxX = max; //document.body.clientWidth;
            can.elements[i].origY = can.elements[i].origY || can.elements[i].y;
            can.elements[i].y = can.elements[i].origY * heightScale;
        }
    });

    ////////////////////////////////////////

    // Adapted from http://bost.ocks.org/mike/algorithms/
    function bestCandidateSampler(width, height, numCandidates) {

        var samples = [];

        function findDistance(a, b) {
            var dx = a[0] - b[0],
                dy = a[1] - b[1];
            return dx * dx + dy * dy;
        }

        function findClosest(c) {
            var i = samples.length,
                sample,
                closest,
                distance,
                closestDistance;

            while (i--) {
                sample = samples[i];
                distance = findDistance(sample, c);

                if (!closestDistance || distance < closestDistance) {
                    closest = sample;
                    closestDistance = distance;
                }
            }

            return closest;
        }

        function getSample() {
            var bestCandidate,
                bestDistance = 0,
                i = 0,
                c, d;

            c = [Math.random() * width, Math.random() * height];

            if (samples.length < 1) {
                bestCandidate = c;
            } else {
                for (; i < numCandidates; i++) {
                    c = [Math.random() * width, Math.random() * height];
                    d = findDistance(findClosest(c), c);

                    if (d > bestDistance) {
                        bestDistance = d;
                        bestCandidate = c;
                    }
                }
            }

            samples.push(bestCandidate);
            //console.log('bestCandidate',bestCandidate);
            return bestCandidate;
        }

        getSample.all = function() {
            return samples;
        };
        getSample.samples = samples;

        return getSample;
    }

    var getCandidate = bestCandidateSampler(width, height, 10);

    var CLOUD_COUNT = 40,
        CLOUD_WIDTH = 510,
        CLOUD_HEIGHT = 260;

    CLOUD_COUNT = Math.floor((width * height) / (CLOUD_WIDTH * CLOUD_HEIGHT));

    var Cloud = Canvallax.createElement({

        init: function(options) {
            this.tex = {
                x: 0,
                y: options.texOffset || 0,
                w: this.image.width,
                h: this.image.height
            };
        },

        render: function(ctx) {
            //this.x = (this.x * this.distance) < this.maxX ? this.x + this.speed : -this.tex.w;
            this.x = (this.x * this.distance) > -this.tex.w ? this.x - this.speed : offsetDistance(this.maxX, this.distance); // / (this.distance || 1);

            ctx.drawImage(this.image, this.tex.x, this.tex.y, this.tex.w, this.tex.h, this.x, this.y, this.tex.w, this.tex.h);
        }

    });

    Cloud.prototype.maxX = width;
    Cloud.prototype.speed = 0.25;


    function offsetDistance(width, distance) {
        var d = (width / distance) / (2 - distance);
        return d;
    }

    function randomRange(min, max) {
        return Math.random() * (max - min) + min;
    }

    function randomizedCloud(image) {

        var canvas = document.createElement('canvas'),
            ctx = canvas.getContext('2d'),
            width = canvas.width = randomRange(400, 700), //CLOUD_WIDTH,
            height = canvas.height = randomRange(200, 260), //CLOUD_HEIGHT,
            w = image.width,
            h = image.height,
            halfw = w / 2,
            halfh = h / 2,
            i = Math.ceil(randomRange(20, 90)), //60
            flip,
            randScale,
            randTex,
            maxScale = 2.5,
            fullPi = Math.PI / 2;

        while (i--) {
            randScale = randomRange(0.4, maxScale);
            ctx.globalAlpha = Math.random() - 0.2;
            ctx.translate(randomRange(halfw, width - (w * maxScale * 1.3)), randomRange(halfh, height - (h * maxScale)));
            ctx.scale(randScale, randomRange(randScale - 0.3, randScale));
            ctx.translate(halfw, halfh);
            ctx.rotate(randomRange(0, fullPi));
            ctx.drawImage(image, -halfw, -halfh); //, w, h, 0, 0, w, h);
            ctx.setTransform(1, 0, 0, 1, 0, 0);
        }


        //document.body.appendChild(canvas);

        //var img = document.createElement('img');
        //img.src = canvas.toDataURL();

        return canvas;
    }

    var cloudImg = new Image();
    cloudImg.addEventListener('load', function() {

        var i = CLOUD_COUNT, //Math.ceil(CLOUD_COUNT * 0.5),
            el, rand, pos, tex;

        while (i--) {
            rand = Math.round(randomRange(0.5, 1.1) * 10) / 10;
            pos = getCandidate();
            tex = randomizedCloud(cloudImg);

            cloud = new Cloud({
                image: tex,
                maxX: width,
                zIndex: rand * 13,
                x: pos[0],
                y: pos[1],
                opacity: (rand < 0.8 ? 0.8 : rand),
                distance: rand,
                speed: rand * randomRange(0.1, 0.3)
            });

            can.addElement(cloud);
        }

        can.render();
    });
    cloudImg.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEYAAABGCAMAAABG8BK2AAAAYFBMVEX///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8GYpHzAAAAIHRSTlMAAwcLDxIWGh8kKzI5QEhPVl9qc3uEi5Sdpa64wcrV4c6KdP8AAAOeSURBVHgBndQJkvM8DoNhS+nv/ieONBH8FIs1nb83ZLfF1wBFZ17vNMZ8fPz79/GY46Xre8F85kRzzhdk/A2TOpSARpF/g0mdaI8XZjg47leA32Jo3wbEooNE/SFGrPOAiPxC+xaDAxBTxQqFoW8wGGof89E4j8nQUceo621h/KY8GuXx4Mg10vRZlPd55JCEnXlIQX7cE8pNp8Dob4oY8LjZTny8QEMo2o2hSqT5YImxchVNbpgZ3oVR4xVUgOlGS5fFKCPSWDY4Yu1xIKyEEqLfE0UUKcoJ9MFVsAhnaOpEGW4gyxFyLitOeRhZO8NJur1hKpWWCV03oaG9yYcYXvD7UPbetVOMNwqlWH6/b7sp29G1Z5g6LFGaY9uYB2A6M7evtVco3U3M1CCopOlNY8Q7cdZahxIMTpv7meR2NghWDqdu8MTZzwMqN+RaBkmdUgf7wMfN1d1cNSAFMdhQ3tLXu2STuclylwYL5QYhsGyLz499bcgxK1F5SmumvaoRrIwSjYutaGbVZIgze6wegLO6i8MD2kJ1N1cYKAUXTLnRWxtnYrMONWRRD+EsA3utw4mnKxNCZRgplK5T05ycvaaZCmtAOEKl+p4ge70k06mcdrQoPgGpbY1EboNyY7/ZHVsfK1BLhBAdCA5MGd719b0gUOJmg9vc5hf3E+K2y1EQDnCjxoGs3t84WiA6zI253rVy6MRnSKNxJtQcRY3xL90MkN6DYGZHI3zBMaF1NcoUQ3Oll+9RBqHb1uIzSTmv9LtQOJbC7Ci/fRsivh0+sBrYwix3GKe8No5yHJTDaZqhqOp8KC6BdmXrFKFaXUUWk7uCLsRPbuAZrmsPjCANBKChIZj/97IBzSJq3pgpymiYRmnxMLG9YbinUGCk5rxbUhJDy/yH+C5U3wP1FQWDL5AtWpNQm0IRz/ys+psCTSKuCObTjY3KhLoCrbUY7ZgIqHRXrTSFHxwfFjcM1fWF8devtJPK2XtM6nAOpcrCXDlVR967qRi6XOY78NJsi95gcsJynMXF2k6gAFFhVFGLz0loz5u0HGoEGF6qOoVgC6cOB6iBb0Ixue66p+p8F+v17VkhUTqGXP6pVptC8JU07z0Ga5VqjmUpvBvuC8wpej4bJiXK+ZHnazfXyfUSipxPVJQvMTjppUKlFUVvv8PIVftrSIRD+Q6DQ7a47wzE9xjaYJk1Fty1v8CYauOLm+fv3Cikjv4lBqVCAP6n/gfZhdXQlm1mfwAAAABJRU5ErkJggg==';



    ////////////////////////////////////////
    // Full cloud texture image

    /*
    var texture = new Image(),
        CLOUD_SPRITE_DISTANCE = 300;

    texture.addEventListener('load', function() {

      //return false;

      var i = Math.ceil(CLOUD_COUNT * 0.5),
          cloud, rand, pos, tex;

      while(i--) {
        rand = Math.round(randomRange(0.3, 0.9) * 10) / 10;
        pos = getCandidate();
        tex = Math.floor(rand < 0.6 ? randomRange(4,6) : randomRange(0,3)) * CLOUD_SPRITE_DISTANCE;

        cloud = new Cloud({
          image: texture,
          tex: {
            x: 0,
            y: tex || 0,
            w: 510,
            h: 260
          },
          maxX: width,
          opacity: (rand < 0.8 ? 0.8 : rand ),
          x: pos[0] - randomRange(0,width * 0.25), //randomRange(-300,window.innerWidth),
          y: pos[1], //Math.ceil((1 - rand) * (CLOUD_SPRITE_COUNT + 1)) * CLOUD_SPRITE_DISTANCE, // Randomize the texture based on distance. Further away clouds are blurry.
          distance: rand, //Math.random()
          speed: rand * randomRange(0.025,0.2),
        });

        can.addElement(cloud);
      }

    });
    texture.src = 'http://i.imgur.com/48yRQIF.png';
    /**/


})();
</script> 

</body>
</html>
"""
        #find#
        nowtoken=""
        for i in range(32):
            nowtoken+=random.choice("abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890")
        token[nowtoken]=Fatherpath+path
        print("add time:",time.time())
        tokentime[nowtoken]=time.time()+15*60
        print(tokentime)
        return """<!DOCTYPE html>
    <html>
    <meta charset="GBK">
    <title>我爱伍屹文件站|文件下载</title>
    <script src="/js/jquery.min.js" type="text/javascript"></script>
    <script src="/js/yzxll.js" type="text/javascript"></script>
    <style>
    #yuanjiao{ 
    font: color:#0FF;
    display: inline-block;
            width: 234px; 
            height:auto; 
    }
    #yuanjiao:hover{
                box-shadow: 0 10px 20px rgba(0,0,0,0.5);
                transform: translateY(-20px);
            }
            
    a.gv { 

            text-decoration:none; 
            background:url(img/but.png) repeat 0px 0px; 
            width: 130px; 
            height: 43px; 
            display: block; 
            text-align:center;		
            line-height:43px; 
            cursor:pointer;
            float:left;
            margin:8px 2px 8px 2px;
            font:18px/43px 'microsoft yahei'; color:#0FF;
            }
    a.gv:hover { 
            background: url(img/but.png) repeat 0px -43px; 
            color:#1d7eb8;
            -webkit-box-shadow: 0 0 6px #1d7eb8;
            transition-duration: 0.5s;
            }
    canvas {
        display: block;
        margin: 2em;
    }
    .bg-canvas {
        position: fixed;
        top: 0;
        left: 0;
        z-index: -1;
        width: 100%;
        height: 100%;
        margin: 0;
    }
    body {
        background-image: -webkit-linear-gradient(bottom, #d7dde6 40%, #97a8c0 80%);
        background-image: linear-gradient(to top, #d7dde6 40%, #97a8c0 80%);
        text-align:center;
        width: auto;
        height: 800vh;
    }
    .footer {
    position: fixed;
    left: 10px;
    bottom: 5px;
    right: 10px; 
    width: 95%;
    color: black;
    text-align: center;
    }
    </style> 
    <body>
<h1 style="font:50px 'microsoft yahei'; color:#0FF;text-align:center;">我爱伍屹文件站文件下载</h1> 
<h2 style="font:color:#0FF;">
	%filename%<br>
	<a href="/filedownload?token=%token%" download="%filename%">点击下载(十五分钟内有效)</a></h2>
	<h6 style="font:color:#0FF;">FileToken:%token%</h6>
    <div class="footer">
    @Copyright 我爱伍屹文件站 开发：一只小流浪(qq3035969948) 运维：伍屹(qq1050661298) 项目地址:<a href="https://github.com/YiZhiXiaoLiuLang/iLoveWuYi">github</a>本站与我爱微软（杨岔路）无任何关系！！！！！！！ 2023 All Right Reserved. 
    <a href="https://beian.miit.gov.cn/" target="_blank" >嘤ICP备114514号</a>
    </div>
    <script>
    (function() {
        var W = window,
            D = document,
            R = D.documentElement,
            B = D.body,
            watchScroll = false,
            WSCROLL = {
                x: 0,
                y: 0
            },
            noop = function() {};

        // Check for canvas support, exit out if no supprt
        if (!W.CanvasRenderingContext2D) {
            return function() {
                return false;
            };
        }

        // Use Init function to keep users from having to use `new Canvallax`. Also keeps Canvallax prototype clean for util functions.
        function Canvallax(options) {
            return new Init(options);
        }

        // Only one scroll tracker that works for every Canvallax instance
        function onScroll() {
            WSCROLL.x = R.scrollLeft || B.scrollLeft;
            WSCROLL.y = R.scrollTop || B.scrollTop;
        }

        function Init(options) {

            var C = this;

            if (!watchScroll) {
                watchScroll = true;
                onScroll();
                W.addEventListener('scroll', onScroll);
            }

            if (options) {
                Canvallax.extend(this, options);
            }

            C.canvas = D.createElement('canvas');
            C.canvas.className = 'canvallax ' + C.className;
            C.parent.insertBefore(C.canvas, C.parent.firstChild);

            if (C.fullscreen) {
                C.resizeFullscreen();
                W.addEventListener('resize', C.resizeFullscreen.bind(C));
            } else {
                C.canvas.width = C.width;
                C.canvas.height = C.height;
            }

            C.ctx = C.canvas.getContext('2d');
            C.x = (options.x !== undefined ? options.x : WSCROLL.x);
            C.y = (options.y !== undefined ? options.y : WSCROLL.y);

            C.addElements(C.elements);
            C.damping = (!C.damping || C.damping < 1 ? 1 : C.damping);

            if (C.animating) {
                C.render();
            }

            return C;
        }


        ////////////////////////////////////////


        function zIndexSort(a, b) {
            return (a.zIndex === b.zIndex ? 0 : a.zIndex < b.zIndex ? -1 : 1);
        }

        function stop() {
            this.animating = false;
            return this;
        }

        Init.prototype = {
            scroll: true,
            parent: B,
            animating: true,
            elements: [],
            damping: 1,
            _x: 0,
            _y: 0,
            fullscreen: true,
            render: function() {
                var C = this,
                    i = 0,
                    len = C.elements.length,
                    el, distance;

                C.now = Date.now();

                if (C.animating !== false) {
                    requestAnimationFrame(C.render.bind(C));
                }

                if (C.scroll) {
                    C.x = (C.scroll === 'invert' || C.scroll === 'invertx' ? -WSCROLL.x : WSCROLL.x);
                    C.y = (C.scroll === 'invert' || C.scroll === 'inverty' ? -WSCROLL.y : WSCROLL.y);
                }

                C._x += (-C.x - C._x) / C.damping;
                C._y += (-C.y - C._y) / C.damping;

                C.ctx.clearRect(0, 0, C.canvas.width, C.canvas.height);

                for (; i < len; i++) {
                    C.ctx.save();
                    C.elements[i]._render(C.ctx, C);
                    C.ctx.restore();
                }
                return this;
            },

            resizeFullscreen: function() {
                this.canvas.width = W.innerWidth;
                this.canvas.height = W.innerHeight;
                return this;
            },

            addElement: function(element) {
                this.elements.push(element);
                this.elements.sort(zIndexSort);
                return this;
            },

            addElements: function(elements) {
                var i = 0,
                    len = elements.length;
                for (; i < len; i++) {
                    this.addElement(elements[i]);
                }
                return this;
            },

            play: function() {
                this.animation = true;
                this.render();
                return this;
            },

            stop: stop,
            pause: stop
        };


        ////////////////////////////////////////

        Canvallax.extend = function(target) {
            target = target || {};

            var length = arguments.length,
                i = 1;

            if (arguments.length === 1) {
                target = this;
                i = 0;
            }

            for (; i < length; i++) {
                if (!arguments[i]) {
                    continue;
                }
                for (var key in arguments[i]) {
                    if (arguments[i].hasOwnProperty(key)) {
                        target[key] = arguments[i][key];
                    }
                }
            }

            return target;
        };

        var elementPrototype = {
            x: 0,
            y: 0,
            opacity: 1,
            distance: 1,
            scale: true,

            render: noop,
            init: noop,

            _render: function(ctx, C) {
                var el = this,
                    distance = el.distance || 1;

                C.ctx.globalAlpha = el.opacity || 1;

                if (el.scale) {
                    C.ctx.scale(distance, distance);
                    C.ctx.translate(C._x, C._y);
                } else {
                    C.ctx.translate(C._x * distance, C._y * distance);
                }

                if (el.render) {
                    el.render.call(el, ctx, C);
                }
            }

        };

        Canvallax.createElement = function(defaults) {

            function elInit(options) {
                Canvallax.extend(this, options);
                this.init.apply(this, arguments);
            }

            function el(options) {
                return new elInit(options);
            }

            elInit.prototype = Canvallax.extend({}, elementPrototype, defaults);
            elInit.prototype.constructor = el;
            return el;
        }

        ////////////////////////////////////////

        Canvallax.Element = Canvallax.createElement();

        ////////////////////////////////////////

        Canvallax.Image = Canvallax.createElement({
            init: function(options) {

                if (options.nodeType === 1) {
                    this.image = options;
                } else if ((!this.image && options.src) || (typeof options === typeof "")) {
                    this.image = new Image();
                    this.image.src = options.src || options;
                }

            },
            render: function(ctx) {

                if (this.image) {
                    var drawArgs = [this.image];

                    if (this.crop) {
                        drawArgs.push(this.crop.x, this.crop.y, this.crop.width, this.crop.height);
                        this.width = (this.width ? this.width : this.crop.width);
                        this.height = (this.height ? this.height : this.crop.height);
                    }

                    drawArgs.push(this.x, this.y);

                    if (this.width && this.height) {
                        drawArgs.push(this.width, this.height);
                    }

                    ctx.drawImage.apply(ctx, drawArgs);
                }
            }
        });

        ////////////////////////////////////////

        return W.Canvallax = Canvallax;

    })();


    var can = Canvallax({
        className: 'bg-canvas',
        scroll: true, // (boolean|'invert'|'invertx'|'inverty') If true, the X and Y of the scene are tied to document's scroll for a typical parallax experience. Set to false if you want to control the scene's X and Y manually.
        x: 0, // Starting x. If tied to scroll, this will be overridden on render.
        y: 0, // Starting y. If tied to scroll, this will be overridden on render.
        damping: 40 // the 'easing' of the x & y position when updated. 1 = none, higher is longer. If you're syncing parallax items to regular items in the scroll, then you'll probably want a low damping.
    });
    /*
      // The canvallax instance can be animated with GSAP, not scroll, if you want!
      TweenMax.to(can,4,{
        //x: 1000,
        y: 1000,
        yoyo: true,
        ease: Cubic.easeInOut,
        repeat: -1,
      });
    */


    // Clouds
    (function() {

        ////////////////////////////////////////


        var origWidth = width = document.body.clientWidth,
            origHeight = height = document.body.clientHeight;

        var gradient = Canvallax.Element({
            width: width * 1.5,
            height: height * 1.1,
            zIndex: 1,
            pattern: (function() {
                var canvas = document.createElement('canvas'),
                    ctx = canvas.getContext('2d'),
                    gradient = ctx.createLinearGradient(0, 0, 0, height);
                gradient.addColorStop(0, '#07588A');
                gradient.addColorStop(1, '#E1F6F4');
                return gradient;
            })(),
            render: function(ctx) {
                ctx.fillStyle = this.pattern;
                ctx.fillRect(this.x, this.y, this.width, this.height);
            }
        });

        can.addElement(gradient);


        window.addEventListener('resize', function() {

            height = document.body.clientHeight;

            var i = can.elements.length,
                max = document.body.clientWidth,
                heightScale = height / origHeight;

            console.log(height, origHeight, heightScale);

            while (i--) {
                can.elements[i].maxX = max; //document.body.clientWidth;
                can.elements[i].origY = can.elements[i].origY || can.elements[i].y;
                can.elements[i].y = can.elements[i].origY * heightScale;
            }
        });

        ////////////////////////////////////////

        // Adapted from http://bost.ocks.org/mike/algorithms/
        function bestCandidateSampler(width, height, numCandidates) {

            var samples = [];

            function findDistance(a, b) {
                var dx = a[0] - b[0],
                    dy = a[1] - b[1];
                return dx * dx + dy * dy;
            }

            function findClosest(c) {
                var i = samples.length,
                    sample,
                    closest,
                    distance,
                    closestDistance;

                while (i--) {
                    sample = samples[i];
                    distance = findDistance(sample, c);

                    if (!closestDistance || distance < closestDistance) {
                        closest = sample;
                        closestDistance = distance;
                    }
                }

                return closest;
            }

            function getSample() {
                var bestCandidate,
                    bestDistance = 0,
                    i = 0,
                    c, d;

                c = [Math.random() * width, Math.random() * height];

                if (samples.length < 1) {
                    bestCandidate = c;
                } else {
                    for (; i < numCandidates; i++) {
                        c = [Math.random() * width, Math.random() * height];
                        d = findDistance(findClosest(c), c);

                        if (d > bestDistance) {
                            bestDistance = d;
                            bestCandidate = c;
                        }
                    }
                }

                samples.push(bestCandidate);
                //console.log('bestCandidate',bestCandidate);
                return bestCandidate;
            }

            getSample.all = function() {
                return samples;
            };
            getSample.samples = samples;

            return getSample;
        }

        var getCandidate = bestCandidateSampler(width, height, 10);

        var CLOUD_COUNT = 40,
            CLOUD_WIDTH = 510,
            CLOUD_HEIGHT = 260;

        CLOUD_COUNT = Math.floor((width * height) / (CLOUD_WIDTH * CLOUD_HEIGHT));

        var Cloud = Canvallax.createElement({

            init: function(options) {
                this.tex = {
                    x: 0,
                    y: options.texOffset || 0,
                    w: this.image.width,
                    h: this.image.height
                };
            },

            render: function(ctx) {
                //this.x = (this.x * this.distance) < this.maxX ? this.x + this.speed : -this.tex.w;
                this.x = (this.x * this.distance) > -this.tex.w ? this.x - this.speed : offsetDistance(this.maxX, this.distance); // / (this.distance || 1);

                ctx.drawImage(this.image, this.tex.x, this.tex.y, this.tex.w, this.tex.h, this.x, this.y, this.tex.w, this.tex.h);
            }

        });

        Cloud.prototype.maxX = width;
        Cloud.prototype.speed = 0.25;


        function offsetDistance(width, distance) {
            var d = (width / distance) / (2 - distance);
            return d;
        }

        function randomRange(min, max) {
            return Math.random() * (max - min) + min;
        }

        function randomizedCloud(image) {

            var canvas = document.createElement('canvas'),
                ctx = canvas.getContext('2d'),
                width = canvas.width = randomRange(400, 700), //CLOUD_WIDTH,
                height = canvas.height = randomRange(200, 260), //CLOUD_HEIGHT,
                w = image.width,
                h = image.height,
                halfw = w / 2,
                halfh = h / 2,
                i = Math.ceil(randomRange(20, 90)), //60
                flip,
                randScale,
                randTex,
                maxScale = 2.5,
                fullPi = Math.PI / 2;

            while (i--) {
                randScale = randomRange(0.4, maxScale);
                ctx.globalAlpha = Math.random() - 0.2;
                ctx.translate(randomRange(halfw, width - (w * maxScale * 1.3)), randomRange(halfh, height - (h * maxScale)));
                ctx.scale(randScale, randomRange(randScale - 0.3, randScale));
                ctx.translate(halfw, halfh);
                ctx.rotate(randomRange(0, fullPi));
                ctx.drawImage(image, -halfw, -halfh); //, w, h, 0, 0, w, h);
                ctx.setTransform(1, 0, 0, 1, 0, 0);
            }


            //document.body.appendChild(canvas);

            //var img = document.createElement('img');
            //img.src = canvas.toDataURL();

            return canvas;
        }

        var cloudImg = new Image();
        cloudImg.addEventListener('load', function() {

            var i = CLOUD_COUNT, //Math.ceil(CLOUD_COUNT * 0.5),
                el, rand, pos, tex;

            while (i--) {
                rand = Math.round(randomRange(0.5, 1.1) * 10) / 10;
                pos = getCandidate();
                tex = randomizedCloud(cloudImg);

                cloud = new Cloud({
                    image: tex,
                    maxX: width,
                    zIndex: rand * 13,
                    x: pos[0],
                    y: pos[1],
                    opacity: (rand < 0.8 ? 0.8 : rand),
                    distance: rand,
                    speed: rand * randomRange(0.1, 0.3)
                });

                can.addElement(cloud);
            }

            can.render();
        });
        cloudImg.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEYAAABGCAMAAABG8BK2AAAAYFBMVEX///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8GYpHzAAAAIHRSTlMAAwcLDxIWGh8kKzI5QEhPVl9qc3uEi5Sdpa64wcrV4c6KdP8AAAOeSURBVHgBndQJkvM8DoNhS+nv/ieONBH8FIs1nb83ZLfF1wBFZ17vNMZ8fPz79/GY46Xre8F85kRzzhdk/A2TOpSARpF/g0mdaI8XZjg47leA32Jo3wbEooNE/SFGrPOAiPxC+xaDAxBTxQqFoW8wGGof89E4j8nQUceo621h/KY8GuXx4Mg10vRZlPd55JCEnXlIQX7cE8pNp8Dob4oY8LjZTny8QEMo2o2hSqT5YImxchVNbpgZ3oVR4xVUgOlGS5fFKCPSWDY4Yu1xIKyEEqLfE0UUKcoJ9MFVsAhnaOpEGW4gyxFyLitOeRhZO8NJur1hKpWWCV03oaG9yYcYXvD7UPbetVOMNwqlWH6/b7sp29G1Z5g6LFGaY9uYB2A6M7evtVco3U3M1CCopOlNY8Q7cdZahxIMTpv7meR2NghWDqdu8MTZzwMqN+RaBkmdUgf7wMfN1d1cNSAFMdhQ3tLXu2STuclylwYL5QYhsGyLz499bcgxK1F5SmumvaoRrIwSjYutaGbVZIgze6wegLO6i8MD2kJ1N1cYKAUXTLnRWxtnYrMONWRRD+EsA3utw4mnKxNCZRgplK5T05ycvaaZCmtAOEKl+p4ge70k06mcdrQoPgGpbY1EboNyY7/ZHVsfK1BLhBAdCA5MGd719b0gUOJmg9vc5hf3E+K2y1EQDnCjxoGs3t84WiA6zI253rVy6MRnSKNxJtQcRY3xL90MkN6DYGZHI3zBMaF1NcoUQ3Oll+9RBqHb1uIzSTmv9LtQOJbC7Ci/fRsivh0+sBrYwix3GKe8No5yHJTDaZqhqOp8KC6BdmXrFKFaXUUWk7uCLsRPbuAZrmsPjCANBKChIZj/97IBzSJq3pgpymiYRmnxMLG9YbinUGCk5rxbUhJDy/yH+C5U3wP1FQWDL5AtWpNQm0IRz/ys+psCTSKuCObTjY3KhLoCrbUY7ZgIqHRXrTSFHxwfFjcM1fWF8devtJPK2XtM6nAOpcrCXDlVR967qRi6XOY78NJsi95gcsJynMXF2k6gAFFhVFGLz0loz5u0HGoEGF6qOoVgC6cOB6iBb0Ixue66p+p8F+v17VkhUTqGXP6pVptC8JU07z0Ga5VqjmUpvBvuC8wpej4bJiXK+ZHnazfXyfUSipxPVJQvMTjppUKlFUVvv8PIVftrSIRD+Q6DQ7a47wzE9xjaYJk1Fty1v8CYauOLm+fv3Cikjv4lBqVCAP6n/gfZhdXQlm1mfwAAAABJRU5ErkJggg==';



        ////////////////////////////////////////
        // Full cloud texture image

        /*
        var texture = new Image(),
            CLOUD_SPRITE_DISTANCE = 300;

        texture.addEventListener('load', function() {

          //return false;

          var i = Math.ceil(CLOUD_COUNT * 0.5),
              cloud, rand, pos, tex;

          while(i--) {
            rand = Math.round(randomRange(0.3, 0.9) * 10) / 10;
            pos = getCandidate();
            tex = Math.floor(rand < 0.6 ? randomRange(4,6) : randomRange(0,3)) * CLOUD_SPRITE_DISTANCE;

            cloud = new Cloud({
              image: texture,
              tex: {
                x: 0,
                y: tex || 0,
                w: 510,
                h: 260
              },
              maxX: width,
              opacity: (rand < 0.8 ? 0.8 : rand ),
              x: pos[0] - randomRange(0,width * 0.25), //randomRange(-300,window.innerWidth),
              y: pos[1], //Math.ceil((1 - rand) * (CLOUD_SPRITE_COUNT + 1)) * CLOUD_SPRITE_DISTANCE, // Randomize the texture based on distance. Further away clouds are blurry.
              distance: rand, //Math.random()
              speed: rand * randomRange(0.025,0.2),
            });

            can.addElement(cloud);
          }

        });
        texture.src = 'http://i.imgur.com/48yRQIF.png';
        /**/


    })();
    </script> 

    </body>
    </html>""".replace("%token%",nowtoken).replace("%filename%",path.split("/")[-1])
    pathbak=path
    path = Fatherpath+path
    
    for file_name in os.listdir(path):
        print(Fatherpath+path+file_name)
        now=fc
        if(os.path.isfile(path+"/"+file_name)):
            now=now.replace("flogo.png","flogo2.png")
        if(len(file_name)>=10):
            
            now=now.replace("我爱伍屹文件站 yyds",file_name[:10]+"...").replace("我爱伍屹文件站 114514","/file"+pathbak+'/'+file_name)
        else:
            now=now.replace("我爱伍屹文件站 yyds",file_name).replace("我爱伍屹文件站 114514","/file"+pathbak+'/'+file_name)
        
        fa+=now
    fa=fa+fb
    return fa


class RequestHandler(BaseHTTPRequestHandler):
    
        
    # ...页面模板...
    Page = '''\
    <html><meta http-equiv="Content-Type" content="text/html; charset=unicode_escape" />
    <body>
​

<p>HELLO!</p>
<p>YiZhiXiaoLiuLang</p>
​
    <table>
    <tr>  <td>Header</td>         <td>NoValue</td>          </tr>
    <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
    <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
    <tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
    <tr>  <td>Command</td>        <td>{command}</td>      </tr>
    <tr>  <td>Path</td>           <td>{path}</td>         </tr>
    <tr>  <td>CPUtemp</td>        <td>{cpu_temp}</td>         </tr>
    </table>
    </body>
    </html>
    '''
    def read_cpu_temp(self):
        with open("/sys/class/thermal/thermal_zone0/temp","r") as f:
            temp=int(f.read())
            temp/=1000
            return temp
            
            

    def do_GET(self):
        print(urllib.parse.unquote(self.path))
        if(self.path[:6]=="/admin"):
            print("转发到fadmin...")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            #self.send_header("Content-Length", "100")
            self.end_headers()
            self.wfile.write(fadmin(urllib.parse.unquote(self.path)).encode('GBK'))
            return
        if(self.path[:13]=="/filedownload"):
            try:
                usertoken=self.path.split("?token=")[-1]
                with open(token[usertoken],"rb") as f:
                    
                    self.send_response(200)
                    self.send_header("Content-type", "file")
                    #self.send_header("Content-Length", "100")
                    self.end_headers()
                    self.wfile.write(f.read())
            except:
                self.send_response(404)
                self.send_header("Content-type", "text")
                #self.send_header("Content-Length", "100")
                self.end_headers()
                self.wfile.write("token错误".encode('GBK'))
            return
        if(self.path[:5]=="/file"):
            try:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                #self.send_header("Content-Length", "100")
                self.end_headers()
                self.wfile.write(fileserver(self.path[5:]).encode('GBK'))
                return
            except:
                self.send_response(502)
                self.send_header("Content-type", "text")
                #self.send_header("Content-Length", "100")
                self.end_headers()
                self.wfile.write("文件访问错误".encode('GBK'))
                return
        if(self.path[:8]=="/teacher"):
            try:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                #self.send_header("Content-Length", "100")
                self.end_headers()
                self.wfile.write(teacher(self.path).encode('GBK'))
                return
            except:
                self.send_response(502)
                self.send_header("Content-type", "text")
                #self.send_header("Content-Length", "100")
                self.end_headers()
                self.wfile.write("文件读取错误".encode('GBK'))
                return
        if(self.path=="/teach"):
            #f2#
            hhh="""<!DOCTYPE html>
    <html>
    <meta charset="GBK">
    <title>我爱伍屹文件站|教程专区</title>
    <script src="js/jquery.min.js" type="text/javascript"></script>
    <script src="js/yzxll.js" type="text/javascript"></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
    #yuanjiao{ 
    font: color:#0FF;
    display: inline-block;
            width: 234px; 
            height:auto; 
    }
    #yuanjiao:hover{
                box-shadow: 0 10px 20px rgba(0,0,0,0.5);
                transform: translateY(-20px);
            }
            
    a.gv { 

            text-decoration:none; 
            background:url(img/but.png) repeat 0px 0px; 
            width: 130px; 
            height: 43px; 
            display: block; 
            text-align:center;		
            line-height:43px; 
            cursor:pointer;
            float:left;
            margin:8px 2px 8px 2px;
            font:18px/43px 'microsoft yahei'; color:#0FF;
            }
    a.gv:hover { 
            background: url(img/but.png) repeat 0px -43px; 
            color:#1d7eb8;
            -webkit-box-shadow: 0 0 6px #1d7eb8;
            transition-duration: 0.5s;
            }
    canvas {
        display: block;
        margin: 2em;
    }
    .bg-canvas {
        position: fixed;
        top: 0;
        left: 0;
        z-index: -1;
        width: 100%;
        height: 100%;
        margin: 0;
    }
    body {
        background-image: -webkit-linear-gradient(bottom, #d7dde6 40%, #97a8c0 80%);
        background-image: linear-gradient(to top, #d7dde6 40%, #97a8c0 80%);
        text-align:center;
        width: auto;
        height: 1000vh;
    }
    .footer {
    position: fixed;
    left: 10px;
    bottom: 5px;
    right: 10px; 
    width: 95%;
    color: black;
    text-align: center;
    }
.btt {
text-align: center;
background: rgba(0,255,255,0.3);

        height:60px;
margin:20px 10%;
padding: 1% 2%
}
    </style> 
    <body>
<h1 style="font:50px 'microsoft yahei'; color:#0FF;text-align:center;">我爱伍屹文件站|教程专区</h1>
"""
            hhh2="""

    <div class="footer">
    @Copyright 我爱伍屹文件站 开发：一只小流浪(qq3035969948) 运维：伍屹(qq1050661298) 项目地址:<a href="https://github.com/YiZhiXiaoLiuLang/iLoveWuYi">github</a>本站与我爱微软（杨岔路）无任何关系！！！！！！！ 2023 All Right Reserved. 
    <a href="https://beian.miit.gov.cn/" target="_blank" >嘤ICP备114514号</a>
    </div>
    <script>
    (function() {
        var W = window,
            D = document,
            R = D.documentElement,
            B = D.body,
            watchScroll = false,
            WSCROLL = {
                x: 0,
                y: 0
            },
            noop = function() {};

        // Check for canvas support, exit out if no supprt
        if (!W.CanvasRenderingContext2D) {
            return function() {
                return false;
            };
        }

        // Use Init function to keep users from having to use `new Canvallax`. Also keeps Canvallax prototype clean for util functions.
        function Canvallax(options) {
            return new Init(options);
        }

        // Only one scroll tracker that works for every Canvallax instance
        function onScroll() {
            WSCROLL.x = R.scrollLeft || B.scrollLeft;
            WSCROLL.y = R.scrollTop || B.scrollTop;
        }

        function Init(options) {

            var C = this;

            if (!watchScroll) {
                watchScroll = true;
                onScroll();
                W.addEventListener('scroll', onScroll);
            }

            if (options) {
                Canvallax.extend(this, options);
            }

            C.canvas = D.createElement('canvas');
            C.canvas.className = 'canvallax ' + C.className;
            C.parent.insertBefore(C.canvas, C.parent.firstChild);

            if (C.fullscreen) {
                C.resizeFullscreen();
                W.addEventListener('resize', C.resizeFullscreen.bind(C));
            } else {
                C.canvas.width = C.width;
                C.canvas.height = C.height;
            }

            C.ctx = C.canvas.getContext('2d');
            C.x = (options.x !== undefined ? options.x : WSCROLL.x);
            C.y = (options.y !== undefined ? options.y : WSCROLL.y);

            C.addElements(C.elements);
            C.damping = (!C.damping || C.damping < 1 ? 1 : C.damping);

            if (C.animating) {
                C.render();
            }

            return C;
        }


        ////////////////////////////////////////


        function zIndexSort(a, b) {
            return (a.zIndex === b.zIndex ? 0 : a.zIndex < b.zIndex ? -1 : 1);
        }

        function stop() {
            this.animating = false;
            return this;
        }

        Init.prototype = {
            scroll: true,
            parent: B,
            animating: true,
            elements: [],
            damping: 1,
            _x: 0,
            _y: 0,
            fullscreen: true,
            render: function() {
                var C = this,
                    i = 0,
                    len = C.elements.length,
                    el, distance;

                C.now = Date.now();

                if (C.animating !== false) {
                    requestAnimationFrame(C.render.bind(C));
                }

                if (C.scroll) {
                    C.x = (C.scroll === 'invert' || C.scroll === 'invertx' ? -WSCROLL.x : WSCROLL.x);
                    C.y = (C.scroll === 'invert' || C.scroll === 'inverty' ? -WSCROLL.y : WSCROLL.y);
                }

                C._x += (-C.x - C._x) / C.damping;
                C._y += (-C.y - C._y) / C.damping;

                C.ctx.clearRect(0, 0, C.canvas.width, C.canvas.height);

                for (; i < len; i++) {
                    C.ctx.save();
                    C.elements[i]._render(C.ctx, C);
                    C.ctx.restore();
                }
                return this;
            },

            resizeFullscreen: function() {
                this.canvas.width = W.innerWidth;
                this.canvas.height = W.innerHeight;
                return this;
            },

            addElement: function(element) {
                this.elements.push(element);
                this.elements.sort(zIndexSort);
                return this;
            },

            addElements: function(elements) {
                var i = 0,
                    len = elements.length;
                for (; i < len; i++) {
                    this.addElement(elements[i]);
                }
                return this;
            },

            play: function() {
                this.animation = true;
                this.render();
                return this;
            },

            stop: stop,
            pause: stop
        };


        ////////////////////////////////////////

        Canvallax.extend = function(target) {
            target = target || {};

            var length = arguments.length,
                i = 1;

            if (arguments.length === 1) {
                target = this;
                i = 0;
            }

            for (; i < length; i++) {
                if (!arguments[i]) {
                    continue;
                }
                for (var key in arguments[i]) {
                    if (arguments[i].hasOwnProperty(key)) {
                        target[key] = arguments[i][key];
                    }
                }
            }

            return target;
        };

        var elementPrototype = {
            x: 0,
            y: 0,
            opacity: 1,
            distance: 1,
            scale: true,

            render: noop,
            init: noop,

            _render: function(ctx, C) {
                var el = this,
                    distance = el.distance || 1;

                C.ctx.globalAlpha = el.opacity || 1;

                if (el.scale) {
                    C.ctx.scale(distance, distance);
                    C.ctx.translate(C._x, C._y);
                } else {
                    C.ctx.translate(C._x * distance, C._y * distance);
                }

                if (el.render) {
                    el.render.call(el, ctx, C);
                }
            }

        };

        Canvallax.createElement = function(defaults) {

            function elInit(options) {
                Canvallax.extend(this, options);
                this.init.apply(this, arguments);
            }

            function el(options) {
                return new elInit(options);
            }

            elInit.prototype = Canvallax.extend({}, elementPrototype, defaults);
            elInit.prototype.constructor = el;
            return el;
        }

        ////////////////////////////////////////

        Canvallax.Element = Canvallax.createElement();

        ////////////////////////////////////////

        Canvallax.Image = Canvallax.createElement({
            init: function(options) {

                if (options.nodeType === 1) {
                    this.image = options;
                } else if ((!this.image && options.src) || (typeof options === typeof "")) {
                    this.image = new Image();
                    this.image.src = options.src || options;
                }

            },
            render: function(ctx) {

                if (this.image) {
                    var drawArgs = [this.image];

                    if (this.crop) {
                        drawArgs.push(this.crop.x, this.crop.y, this.crop.width, this.crop.height);
                        this.width = (this.width ? this.width : this.crop.width);
                        this.height = (this.height ? this.height : this.crop.height);
                    }

                    drawArgs.push(this.x, this.y);

                    if (this.width && this.height) {
                        drawArgs.push(this.width, this.height);
                    }

                    ctx.drawImage.apply(ctx, drawArgs);
                }
            }
        });

        ////////////////////////////////////////

        return W.Canvallax = Canvallax;

    })();


    var can = Canvallax({
        className: 'bg-canvas',
        scroll: true, // (boolean|'invert'|'invertx'|'inverty') If true, the X and Y of the scene are tied to document's scroll for a typical parallax experience. Set to false if you want to control the scene's X and Y manually.
        x: 0, // Starting x. If tied to scroll, this will be overridden on render.
        y: 0, // Starting y. If tied to scroll, this will be overridden on render.
        damping: 40 // the 'easing' of the x & y position when updated. 1 = none, higher is longer. If you're syncing parallax items to regular items in the scroll, then you'll probably want a low damping.
    });
    /*
      // The canvallax instance can be animated with GSAP, not scroll, if you want!
      TweenMax.to(can,4,{
        //x: 1000,
        y: 1000,
        yoyo: true,
        ease: Cubic.easeInOut,
        repeat: -1,
      });
    */


    // Clouds
    (function() {

        ////////////////////////////////////////


        var origWidth = width = document.body.clientWidth,
            origHeight = height = document.body.clientHeight;

        var gradient = Canvallax.Element({
            width: width * 1.5,
            height: height * 1.1,
            zIndex: 1,
            pattern: (function() {
                var canvas = document.createElement('canvas'),
                    ctx = canvas.getContext('2d'),
                    gradient = ctx.createLinearGradient(0, 0, 0, height);
                gradient.addColorStop(0, '#07588A');
                gradient.addColorStop(1, '#E1F6F4');
                return gradient;
            })(),
            render: function(ctx) {
                ctx.fillStyle = this.pattern;
                ctx.fillRect(this.x, this.y, this.width, this.height);
            }
        });

        can.addElement(gradient);


        window.addEventListener('resize', function() {

            height = document.body.clientHeight;

            var i = can.elements.length,
                max = document.body.clientWidth,
                heightScale = height / origHeight;

            console.log(height, origHeight, heightScale);

            while (i--) {
                can.elements[i].maxX = max; //document.body.clientWidth;
                can.elements[i].origY = can.elements[i].origY || can.elements[i].y;
                can.elements[i].y = can.elements[i].origY * heightScale;
            }
        });

        ////////////////////////////////////////

        // Adapted from http://bost.ocks.org/mike/algorithms/
        function bestCandidateSampler(width, height, numCandidates) {

            var samples = [];

            function findDistance(a, b) {
                var dx = a[0] - b[0],
                    dy = a[1] - b[1];
                return dx * dx + dy * dy;
            }

            function findClosest(c) {
                var i = samples.length,
                    sample,
                    closest,
                    distance,
                    closestDistance;

                while (i--) {
                    sample = samples[i];
                    distance = findDistance(sample, c);

                    if (!closestDistance || distance < closestDistance) {
                        closest = sample;
                        closestDistance = distance;
                    }
                }

                return closest;
            }

            function getSample() {
                var bestCandidate,
                    bestDistance = 0,
                    i = 0,
                    c, d;

                c = [Math.random() * width, Math.random() * height];

                if (samples.length < 1) {
                    bestCandidate = c;
                } else {
                    for (; i < numCandidates; i++) {
                        c = [Math.random() * width, Math.random() * height];
                        d = findDistance(findClosest(c), c);

                        if (d > bestDistance) {
                            bestDistance = d;
                            bestCandidate = c;
                        }
                    }
                }

                samples.push(bestCandidate);
                //console.log('bestCandidate',bestCandidate);
                return bestCandidate;
            }

            getSample.all = function() {
                return samples;
            };
            getSample.samples = samples;

            return getSample;
        }

        var getCandidate = bestCandidateSampler(width, height, 10);

        var CLOUD_COUNT = 40,
            CLOUD_WIDTH = 510,
            CLOUD_HEIGHT = 260;

        CLOUD_COUNT = Math.floor((width * height) / (CLOUD_WIDTH * CLOUD_HEIGHT));

        var Cloud = Canvallax.createElement({

            init: function(options) {
                this.tex = {
                    x: 0,
                    y: options.texOffset || 0,
                    w: this.image.width,
                    h: this.image.height
                };
            },

            render: function(ctx) {
                //this.x = (this.x * this.distance) < this.maxX ? this.x + this.speed : -this.tex.w;
                this.x = (this.x * this.distance) > -this.tex.w ? this.x - this.speed : offsetDistance(this.maxX, this.distance); // / (this.distance || 1);

                ctx.drawImage(this.image, this.tex.x, this.tex.y, this.tex.w, this.tex.h, this.x, this.y, this.tex.w, this.tex.h);
            }

        });

        Cloud.prototype.maxX = width;
        Cloud.prototype.speed = 0.25;


        function offsetDistance(width, distance) {
            var d = (width / distance) / (2 - distance);
            return d;
        }

        function randomRange(min, max) {
            return Math.random() * (max - min) + min;
        }

        function randomizedCloud(image) {

            var canvas = document.createElement('canvas'),
                ctx = canvas.getContext('2d'),
                width = canvas.width = randomRange(400, 700), //CLOUD_WIDTH,
                height = canvas.height = randomRange(200, 260), //CLOUD_HEIGHT,
                w = image.width,
                h = image.height,
                halfw = w / 2,
                halfh = h / 2,
                i = Math.ceil(randomRange(20, 90)), //60
                flip,
                randScale,
                randTex,
                maxScale = 2.5,
                fullPi = Math.PI / 2;

            while (i--) {
                randScale = randomRange(0.4, maxScale);
                ctx.globalAlpha = Math.random() - 0.2;
                ctx.translate(randomRange(halfw, width - (w * maxScale * 1.3)), randomRange(halfh, height - (h * maxScale)));
                ctx.scale(randScale, randomRange(randScale - 0.3, randScale));
                ctx.translate(halfw, halfh);
                ctx.rotate(randomRange(0, fullPi));
                ctx.drawImage(image, -halfw, -halfh); //, w, h, 0, 0, w, h);
                ctx.setTransform(1, 0, 0, 1, 0, 0);
            }


            //document.body.appendChild(canvas);

            //var img = document.createElement('img');
            //img.src = canvas.toDataURL();

            return canvas;
        }

        var cloudImg = new Image();
        cloudImg.addEventListener('load', function() {

            var i = CLOUD_COUNT, //Math.ceil(CLOUD_COUNT * 0.5),
                el, rand, pos, tex;

            while (i--) {
                rand = Math.round(randomRange(0.5, 1.1) * 10) / 10;
                pos = getCandidate();
                tex = randomizedCloud(cloudImg);

                cloud = new Cloud({
                    image: tex,
                    maxX: width,
                    zIndex: rand * 13,
                    x: pos[0],
                    y: pos[1],
                    opacity: (rand < 0.8 ? 0.8 : rand),
                    distance: rand,
                    speed: rand * randomRange(0.1, 0.3)
                });

                can.addElement(cloud);
            }

            can.render();
        });
        cloudImg.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEYAAABGCAMAAABG8BK2AAAAYFBMVEX///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8GYpHzAAAAIHRSTlMAAwcLDxIWGh8kKzI5QEhPVl9qc3uEi5Sdpa64wcrV4c6KdP8AAAOeSURBVHgBndQJkvM8DoNhS+nv/ieONBH8FIs1nb83ZLfF1wBFZ17vNMZ8fPz79/GY46Xre8F85kRzzhdk/A2TOpSARpF/g0mdaI8XZjg47leA32Jo3wbEooNE/SFGrPOAiPxC+xaDAxBTxQqFoW8wGGof89E4j8nQUceo621h/KY8GuXx4Mg10vRZlPd55JCEnXlIQX7cE8pNp8Dob4oY8LjZTny8QEMo2o2hSqT5YImxchVNbpgZ3oVR4xVUgOlGS5fFKCPSWDY4Yu1xIKyEEqLfE0UUKcoJ9MFVsAhnaOpEGW4gyxFyLitOeRhZO8NJur1hKpWWCV03oaG9yYcYXvD7UPbetVOMNwqlWH6/b7sp29G1Z5g6LFGaY9uYB2A6M7evtVco3U3M1CCopOlNY8Q7cdZahxIMTpv7meR2NghWDqdu8MTZzwMqN+RaBkmdUgf7wMfN1d1cNSAFMdhQ3tLXu2STuclylwYL5QYhsGyLz499bcgxK1F5SmumvaoRrIwSjYutaGbVZIgze6wegLO6i8MD2kJ1N1cYKAUXTLnRWxtnYrMONWRRD+EsA3utw4mnKxNCZRgplK5T05ycvaaZCmtAOEKl+p4ge70k06mcdrQoPgGpbY1EboNyY7/ZHVsfK1BLhBAdCA5MGd719b0gUOJmg9vc5hf3E+K2y1EQDnCjxoGs3t84WiA6zI253rVy6MRnSKNxJtQcRY3xL90MkN6DYGZHI3zBMaF1NcoUQ3Oll+9RBqHb1uIzSTmv9LtQOJbC7Ci/fRsivh0+sBrYwix3GKe8No5yHJTDaZqhqOp8KC6BdmXrFKFaXUUWk7uCLsRPbuAZrmsPjCANBKChIZj/97IBzSJq3pgpymiYRmnxMLG9YbinUGCk5rxbUhJDy/yH+C5U3wP1FQWDL5AtWpNQm0IRz/ys+psCTSKuCObTjY3KhLoCrbUY7ZgIqHRXrTSFHxwfFjcM1fWF8devtJPK2XtM6nAOpcrCXDlVR967qRi6XOY78NJsi95gcsJynMXF2k6gAFFhVFGLz0loz5u0HGoEGF6qOoVgC6cOB6iBb0Ixue66p+p8F+v17VkhUTqGXP6pVptC8JU07z0Ga5VqjmUpvBvuC8wpej4bJiXK+ZHnazfXyfUSipxPVJQvMTjppUKlFUVvv8PIVftrSIRD+Q6DQ7a47wzE9xjaYJk1Fty1v8CYauOLm+fv3Cikjv4lBqVCAP6n/gfZhdXQlm1mfwAAAABJRU5ErkJggg==';



        ////////////////////////////////////////
        // Full cloud texture image

        /*
        var texture = new Image(),
            CLOUD_SPRITE_DISTANCE = 300;

        texture.addEventListener('load', function() {

          //return false;

          var i = Math.ceil(CLOUD_COUNT * 0.5),
              cloud, rand, pos, tex;

          while(i--) {
            rand = Math.round(randomRange(0.3, 0.9) * 10) / 10;
            pos = getCandidate();
            tex = Math.floor(rand < 0.6 ? randomRange(4,6) : randomRange(0,3)) * CLOUD_SPRITE_DISTANCE;

            cloud = new Cloud({
              image: texture,
              tex: {
                x: 0,
                y: tex || 0,
                w: 510,
                h: 260
              },
              maxX: width,
              opacity: (rand < 0.8 ? 0.8 : rand ),
              x: pos[0] - randomRange(0,width * 0.25), //randomRange(-300,window.innerWidth),
              y: pos[1], //Math.ceil((1 - rand) * (CLOUD_SPRITE_COUNT + 1)) * CLOUD_SPRITE_DISTANCE, // Randomize the texture based on distance. Further away clouds are blurry.
              distance: rand, //Math.random()
              speed: rand * randomRange(0.025,0.2),
            });

            can.addElement(cloud);
          }

        });
        texture.src = 'http://i.imgur.com/48yRQIF.png';
        /**/


    })();
    </script> 

    </body>
    </html>
"""
            hhh3=""#<div class="btt"><p>一只小流浪</p></div>
            for file_name in os.listdir("teach/"):
                if(file_name=="index.html"):
                    continue
                hhh3=hhh3+"<a href=\"/teacher?%filename%\" style=\"text-decoration: none;\"><div class=\"btt\"><p>%title%</p></div><a>".replace("%title%",file_name.replace(".md","")).replace("%filename%",urllib.parse.quote(file_name))
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            #self.send_header("Content-Length", "100")
            self.end_headers()
            self.wfile.write((hhh+hhh3+hhh2).encode('GBK'))
            return
            
        values = {
            'date_time'   : self.date_time_string(),
            'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command'     : self.command,
            'path'        : self.path,
            'cpu_temp'    : 'undefine'
            #'cpu_temp'    : self.read_cpu_temp()
        }
        try:#is a file(/dir/file.txt)
            print("二次转义",urllib.parse.unquote(urllib.parse.unquote(self.path[1:])))
            with open(urllib.parse.unquote(self.path[1:]),mode="rb") as f:
                file=f.read()
                print(file)
                self.send_response(200)
                #self.send_header("Content-type", "text/html")
                #self.send_header("Content-Length", "100")
                self.end_headers()
                self.wfile.write(file)
                print(self.path,'file')
                
        except:#is an index.html(/set -> /set/index.html)
            try:
                print(self.path)
                
                with open(self.path[1:]+"index.html",mode="r",encoding="GBK") as f:
                    print(114514)
                    page = self.Page
                    file=f.read()
                    
                    #file=file.format(**values)
                    print(file) 
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    #self.send_header("Content-Length", "100")
                    self.end_headers()
                    
                    self.wfile.write(file.encode('GBK'))
            except Exception as e:
                epage='404 file not found\n\n'+str(e)
                self.send_response(404)
                self.send_header("Content-Length", str(len(epage)))
                self.end_headers()
                self.wfile.write(epage.encode('GBK'))
                
        '''
        if self.path[:5]=="/file":
            res=requests.get(file_host+self.path)
            self.send_response(res.status_code)
            #self.send_header("Content-type","text")
            self.send_header("Content-Length", str(len(res.text)))
            self.end_headers()
            self.wfile.write(res.text.encode('unicode_escape'))
            return
        else:
            page = self.create_page()
        self.send_content(page)
        '''
    def create_page(self):
        values = {
            'date_time'   : self.date_time_string(),
            'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command'     : self.command,
            'path'        : self.path,
            'cpu_temp'    : self.read_cpu_temp()
        }
        page = self.Page.format(**values)
        return page

    def send_content(self, page):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page.encode('GBK'))
threading.Thread(name="CheckToken",target=AutoRemoveToken).start()
        
serverAddress = ('', 8080)
server = HTTPServer(serverAddress, RequestHandler)
server.serve_forever()
