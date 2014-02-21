<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:g="http://base.google.com/ns/1.0">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<script language="javascript">
function toggleoptions() {
    var x = document.getElementById("options");
    if (x.style.display == "block") {
        x.style.display="none";
    } else {
        x.style.display="block";
    }
    return false;
}

function togglelinenumbers() {
    var tds = document.getElementsByTagName("td");
    for (var i = 0; i+1 != tds.length; i++) {
        var els = tds[i].getElementsByClassName("linenodiv");
        if (els.length == 1) {
            if (els[0].style.visibility=="hidden") {
                els[0].style.visibility="visible";
            } else {
                els[0].style.visibility="hidden";
            }
        }
    }
}

</script>
<style type="text/css">
    body {
        font-family: Verdana,Arial,'Bitstream Vera Sans',Helvetica,Sans-serif;
        padding: 0px;
        margin: 0px;
        font-size: 10pt;
        background-color: white;
    }
    div.headerbox {
        text-align: right;
        color: white;
        background: #333;
        padding-right: 1em;
    }
    div.optionsbox {
        position: absolute;
        right: 0;
        background: #333;
        margin: px;
        padding: 0.2em;
        padding-right: 1em;
        display: none;
    }
    ul {
        margin: 0;
        padding: 4px;
    }
    li {
        list-style: none;
        text-align: left;
    }
    p.title {
        font-size: 20pt;
    }
    p {
        margin: 0px;
        padding: 0px;
    }
    a {
        color: #888;
        text-decoration: none;
    }
    a:hover {
        color: #fff;
    }
    td { vertical-align: text-top;}
    td.linenos { text-align: right; color: #888; }
.hll { background-color: #ffffcc }
.c { color: #408080; font-style: italic } /* Comment */
.err { border: 1px solid #FF0000 } /* Error */
.k { color: #008000; font-weight: bold } /* Keyword */
.o { color: #666666 } /* Operator */
.cm { color: #408080; font-style: italic } /* Comment.Multiline */
.cp { color: #BC7A00 } /* Comment.Preproc */
.c1 { color: #408080; font-style: italic } /* Comment.Single */
.cs { color: #408080; font-style: italic } /* Comment.Special */
.gd { color: #A00000 } /* Generic.Deleted */
.ge { font-style: italic } /* Generic.Emph */
.gr { color: #FF0000 } /* Generic.Error */
.gh { color: #000080; font-weight: bold } /* Generic.Heading */
.gi { color: #00A000 } /* Generic.Inserted */
.go { color: #808080 } /* Generic.Output */
.gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.gs { font-weight: bold } /* Generic.Strong */
.gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.gt { color: #0040D0 } /* Generic.Traceback */
.kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.kp { color: #008000 } /* Keyword.Pseudo */
.kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.kt { color: #B00040 } /* Keyword.Type */
.m { color: #666666 } /* Literal.Number */
.s { color: #BA2121 } /* Literal.String */
.na { color: #7D9029 } /* Name.Attribute */
.nb { color: #008000 } /* Name.Builtin */
.nc { color: #0000FF; font-weight: bold } /* Name.Class */
.no { color: #880000 } /* Name.Constant */
.nd { color: #AA22FF } /* Name.Decorator */
.ni { color: #999999; font-weight: bold } /* Name.Entity */
.ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.nf { color: #0000FF } /* Name.Function */
.nl { color: #A0A000 } /* Name.Label */
.nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.nt { color: #008000; font-weight: bold } /* Name.Tag */
.nv { color: #19177C } /* Name.Variable */
.ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.w { color: #bbbbbb } /* Text.Whitespace */
.mf { color: #666666 } /* Literal.Number.Float */
.mh { color: #666666 } /* Literal.Number.Hex */
.mi { color: #666666 } /* Literal.Number.Integer */
.mo { color: #666666 } /* Literal.Number.Oct */
.sb { color: #BA2121 } /* Literal.String.Backtick */
.sc { color: #BA2121 } /* Literal.String.Char */
.sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.s2 { color: #BA2121 } /* Literal.String.Double */
.se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.sh { color: #BA2121 } /* Literal.String.Heredoc */
.si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.sx { color: #008000 } /* Literal.String.Other */
.sr { color: #BB6688 } /* Literal.String.Regex */
.s1 { color: #BA2121 } /* Literal.String.Single */
.ss { color: #19177C } /* Literal.String.Symbol */
.bp { color: #008000 } /* Name.Builtin.Pseudo */
.vc { color: #19177C } /* Name.Variable.Class */
.vg { color: #19177C } /* Name.Variable.Global */
.vi { color: #19177C } /* Name.Variable.Instance */
.il { color: #666666 } /* Literal.Number.Integer.Long */
</style>
<title>paste.se - Unnamed paste (pasted by unknown)</title>
<script src="https://apis.google.com/js/plusone.js" type="text/javascript"></script>
</head>
<body>
  <div class="headerbox">
    <p class="title">Unnamed paste</p>
    <p>
      <span class="pastedby">pasted by</span>
      <span class="who">Unknown</span>
      <a href="/options" onclick="return toggleoptions();">[options]</a>
      <div class="optionsbox" id="options">
    <ul>
      <li><a href="/raw">Show as plain text</a></li>
      <li><a href="javascript:togglelinenumbers();">Toggle linenumbers</a></li>
      <li><a href="http://new.paste.se/">Create new paste</a></li>
      <li style="padding-top: 10px;"><g:plusone></g:plusone></li>
    </ul>
      </div>
    </p>
  </div>
  <table class="sourcetable"><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61</pre></div></td><td class="code"><div class="source"><pre>def McNuggets(n):

six = 0
six_counter = 0
nine = 0
nine_counter = 0
twenty = 0
twenty_counter = 0
x = n
count = 1

while six + nine + twenty != x:
        six = six + 6
        six_counter += 1
        sum = six + nine + twenty
        if six + nine + twenty == x:
                return True
                six = 0
                six_counter = 0
                nine = 0
                nine_counter = 0
                twenty = 0
                twenty_counter = 0
                break
        elif six + nine + twenty > x:
                six = 0
                six_counter = 0
                nine = nine + 9
                nine_counter += 1
                sum = six + nine + twenty
                if six + nine + twenty == x:
                        return True
                        six = 0
                        six_counter = 0
                        nine = 0
                        nine_counter = 0
                        twenty = 0
                        twenty_counter = 0
                        break
                elif six + nine + twenty > x:
                        six = 0
                        six_counter = 0
                        nine = 0
                        nine_counter = 0
                        twenty = twenty + 20
                        twenty_counter += 1
                        if six + nine + twenty == x:
                                return True
                                six = 0
                                six_counter = 0
                                nine = 0
                                nine_counter = 0
                                twenty = 0
                                twenty_counter = 0
                                break
                        elif six + nine + twenty > x:
                                return False
                                six = 0
                                nine = 0
                                twenty = 0
                                break
</pre></div>
</td></tr></table>
</body>
</html>