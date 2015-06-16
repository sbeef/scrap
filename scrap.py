import time

OPEN_HTML = "<HTML>\n"

OPEN_HEADER="\t<HEAD>\n\t\t<TITLE>"
CLOSE_HEADER="</TITLE>\n\t<\HEAD>\n"

OPEN_BODY="\t<BODY>\n"

TITLE_ALIGNMENT = "CENTER"
TITLE_TYPE = "H1"

OPEN_TITLE="\t\t<%s><%s>" % (TITLE_ALIGNMENT, TITLE_TYPE)
CLOSE_TITLE="</%s></%s>\n" % (TITLE_TYPE, TITLE_ALIGNMENT)


def generate_header(post_name):
  return "%s%s%s" % (OPEN_HEADER, post_name, CLOSE_HEADER)

def generate_title(post_name):
  
  

def paste(content, date_string):
  date = time.strptime(date_string, "%d/%m/%y")
  post_name = date.strftime("%d-%m-%Y")
  post_file_name = post_name + ".html"
  post_file = open(post_file_name, 'w')
  post_file.write(OPEN_HTML)
  post_file.write(generate_header(post_name))
  post_file.write(OPEN_BODY)
