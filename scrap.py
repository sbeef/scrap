import datetime
import os

# indentation stuff

HTML_INDENT_LEVEL    = 0
HEAD_INDENT_LEVEL    = 1
TITLE_INDENT_LEVEL   = 2
BODY_INDENT_LEVEL    = 1
HEADING_INDENT_LEVEL = 2
CONTENT_INDENT_LEVEL = 2

def generate_indents(indent_level):
  indents = ""
  for x in xrange(indent_level):
    indents = indents + "\t"
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

CONTENT_ALIGNMENT = "CENTER"

# templates
OPEN_HTML     = "%s<HTML>\n" % (HTML_INDENTS)
CLOSE_HTML    = "%s</HTML>"  % (HTML_INDENTS)

OPEN_HEADER   = "%s<HEAD>\n%s<TITLE>"   % (HEAD_INDENTS, TITLE_INDENTS)
CLOSE_HEADER  = "</TITLE>\n%s</HEAD>\n" % (HEAD_INDENTS)

OPEN_BODY     = "%s<BODY>\n"  % (BODY_INDENTS)
CLOSE_BODY    = "%s</BODY>\n" % (BODY_INDENTS)

OPEN_TITLE    = "%s<%s><%s>"   % (HEADING_INDENTS, HEADING_ALIGNMENT, HEADING_TYPE)
CLOSE_TITLE   = "</%s></%s>\n" % (HEADING_TYPE, HEADING_ALIGNMENT)

OPEN_CONTENT  = "%s<BR/>\n%s<%s><img src=\"" % (CONTENT_INDENTS, CONTENT_INDENTS, CONTENT_ALIGNMENT)
CLOSE_CONTENT = "\"/></%s>\n"           % (CONTENT_ALIGNMENT)


# generators

def generate_header(post_name):
  return "%s%s%s" % (OPEN_HEADER, post_name, CLOSE_HEADER)

def generate_title(post_name):
  return "%s%s%s" % (OPEN_TITLE, post_name, CLOSE_TITLE)

def generate_content(content):
  return "%s%s%s" % (OPEN_CONTENT, content, CLOSE_CONTENT)
  
# set up

def bookkeep_directory(date):
  if not os.path.exists(date):
    os.makedirs(date)

def paste(content, date_string):
  date = datetime.datetime.strptime(date_string, "%m/%d/%y")
  post_name = date.strftime("%m-%d-%Y")
  bookkeep_directory(post_name)
  post_file_name = post_name + "/index.html"
  post_file = open(post_file_name, 'w')
  post_file.write(OPEN_HTML)
  post_file.write(generate_header(post_name))
  post_file.write(OPEN_BODY)
  post_file.write(generate_title(post_name))
  post_file.write(generate_content(content))
  post_file.write(CLOSE_BODY)
  post_file.write(CLOSE_HTML)
  post_file.close()
