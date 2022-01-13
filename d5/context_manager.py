class Tag:
    def __init__(self, tagname):
        self.tagname = tagname
    def __enter__(self):
        print('<{}>'.format(self.tagname))
    def __exit__(self, etype, evalue, etraceback):
        print('</{}>'.format(self.tagname))

html_tag = Tag('HTML')
body_tag = Tag('BODY')
paragraph_tag = Tag('p')

with html_tag:
    with body_tag:
        print('treść dokumentu')

with paragraph_tag:
    print("treść paragrafu")