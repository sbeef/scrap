import time

# indentation stuff

HTML_INDENT_LEVEL    = 0
HEAD_INDENT_LEVEL    = 1
TITLE_INDENT_LEVEL   = 2
BODY_INDENT_LEVEL    = 1
HEADING_INDENT_LEVEL = 2
CONTENT_INDENT_LEVEL = 2

def generate_indents(indent_level):
  indents = ""
  for x in range(indent_level):
    indnets = indents + "\t"
  return indents

HTML_INDENTS    = generate_indents(HTML_INDENT_LEVEL)
HEAD_INDENTS    = generate_indents(HEAD_INDENT_LEVEL)
TITLE_INDENTS   = generate_indents(TITLE_INDENT_LEVEL)
BODY_INDENTS    = generate_indents(BODY_INDENT_LEVEL)
HEADING_INDENTS = generate_indents(HEADING_INDENT_LEVEL)
CONTENT_INDENTS = generate_indents(CONTENT_INDENT_LEVEL)

# element properties
HEADING_ALIGNMENT = "CENTER"
HEADING_TYPE      = "H1"

# templates
OPEN_HTML     = "%s<HTML>\n" % (HTML_INDENTS)
CLOSE_HTML    = "%s</HTML>"  % (HTML_INDENTS)

OPEN_HEADER   = "%s<HEAD>\n%s<TITLE>"   % (HEAD_INDENTS, TITLE_INDENTS)
CLOSE_HEADER  = "</TITLE>\n%s<\HEAD>\n" % (HEAD_INDENTS)

OPEN_BODY     = "%s<BODY>\n"  % (BODY_INDENTS)
CLOSE_BODY    = "%s</BODY>\n" % (BODY_INDENTS)

OPEN_TITLE    = "%s<%s><%s>"   % (HEADING_INDENTS, HEADING_ALIGNMENT, HEADING_TYPE)
CLOSE_TITLE   = "</%s></%s>\n" % (HEADING_TYPE, HEADING_ALIGNMENT)

OPEN_CONTENT  = "%s<BR><%s><img src=\"" % (CONTNET_INDENTS, CONTENT_ALIGNMNET)
CLOSE_CONTENT = "\"/></%s>\n"           % (CONTENT_ALIGNMENT)


# generators

def generate_header(post_name):
  return "%s%s%s" % (OPEN_HEADER, post_name, CLOSE_HEADER)

def generate_title(post_name):
  return "%s%s%s" % (OPEN_TITLE, post_name, CLOSE_TITLE)

def generate_content(content):
  return "%s%s%s" % (OPEN_CONTENT, content, CLOSE_CONTENT)
  
def paste(content, date_string):
  date = time.strptime(date_string, "%d/%m/%y")
  post_name = date.strftime("%d-%m-%Y")
  post_file_name = post_name + ".html"
  post_file = open(post_file_name, 'w')
  post_file.write(OPEN_HTML)
  post_file.write(generate_header(post_name))
  post_file.write(OPEN_BODY)
  post_file.write(generate_title(post_name))

