PRE = "https://github.com/MER-wiki/pdf_version/blob/gh-pages/pdfs/"
POST = "?raw=true"
with open('exam_pdf_url.csv', 'r') as fin:
    next(fin)
    with open('table.html', 'w') as fout:
        fout.write('<table style="width:100%">\n')
        for line in fin:
            url, course, exam = line.strip().split(',')
            fout.write('<tr>\n<td>%s</td>\n<td>%s</td>\n' % (course, exam))
            raw_link = '%s_%s' % (course, exam)
            fout.write(
                ('<td><a id="%s_%s_e" href="%s">'
                 'Original exam</a></td>\n' % (course, exam,
                                               url)))
            fout.write(
                ('<td><a id="%s_%s_a" href="%s%s_Answers.pdf%s">'
                 'Final Answers</a></td>\n' % (course, exam,
                                               PRE, raw_link, POST)))
            fout.write(('<td><a id="%s_%s_s" href="%s%s_Solutions.pdf%s">'
                        'Full Solutions</a></td>\n</tr>\n' % (course, exam,
                                                              PRE,
                                                              raw_link, POST)))

        fout.write('</table>')


with open('exam_pdf_url.csv', 'r') as fin:
    next(fin)
    with open('javascripts/ga_script.js', 'w') as fout:
        for line in fin:
            url, course, exam = line.strip().split(',')
            identifier_e = '%s_%s_e' % (course, exam)
            identifier_a = '%s_%s_a' % (course, exam)
            identifier_s = '%s_%s_s' % (course, exam)

            for ide in [identifier_e, identifier_a, identifier_s]:
                fout.write("var %s=document.getElementById('%s');\n" % (ide,
                                                                        ide)
                           )
                fout.write("addListener(%s,'click',function(){\n" % ide)

                fout.write(
                    "ga('send','event','MER_pdf','click','%s');\n" % ide)
                fout.write("});\n")
        fout.write("""
function addListener(element, type, callback) {
  if (element.addEventListener) element.addEventListener(type, callback);
  else if (element.attachEvent) element.attachEvent('on' + type, callback);
}
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-49094053-1', 'ubc.ca');
ga('require', 'linkid', 'linkid.js');
ga('send', 'pageview');
        """)
