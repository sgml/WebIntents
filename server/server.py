import webapp2
from webapp2 import Route
from webapp2_extras import routes

import handlers_base
import registry.handlers
import widgets.handlers
import demos.mememator.handlers
import demos.twitpic.handlers
import demos.shortener.handlers
import demos.instapaper.handlers
import demos.imgur.handlers

import sys
#for attr in ('stdin', 'stdout', 'stderr'):
#  setattr(sys, attr, getattr(sys, '__%s__' % attr))


exampleRoutes = [ Route('/<:.*>', handlers_base.PageHandler, 'examples')]
demoRoutes = [
      Route('/mememator/proxy', demos.mememator.handlers.ProxyHandler, 'demos'),
      Route('/mememator/<:.*>', handlers_base.PageHandler, 'demos'),
      Route('/imagestudio/<:.*>', handlers_base.PageHandler, 'demos'),
      Route('/twitpic/proxy', demos.twitpic.handlers.ProxyHandler, 'demos'),
      Route('/twitpic/upload', demos.twitpic.handlers.UploadHandler, 'demos'),
      Route('/twitpic/<:.*>', handlers_base.PageHandler, 'demos'),
      Route('/shortener/shorten', demos.shortener.handlers.ShortenHandler, 'demos'),
      Route('/shortener/<:.*>', handlers_base.PageHandler, 'demos'),
      Route('/instapaper/add', demos.instapaper.handlers.AddHandler, 'demos'),
      Route('/instapaper/<:.*>', handlers_base.PageHandler, 'demos'),
      Route('/imgur/save', demos.imgur.handlers.SaveHandler, 'demos'),
      Route('/imgur/<:.*>', handlers_base.PageHandler, 'demos'),
      Route('/<:.*>', handlers_base.PageHandler, 'demos')
]

app = webapp2.WSGIApplication([
    routes.DomainRoute('webintents-org.appspot.com', [
      Route('/<:.*>', handlers_base.PageHandler, 'webintents')
    ]),
    routes.DomainRoute('examples.webintents-org.appspot.com', exampleRoutes),
    routes.DomainRoute('examples.webintents.org', exampleRoutes),
    routes.DomainRoute('demos.webintents-org.appspot.com', demoRoutes ),
    routes.DomainRoute('demos.webintents.org', demoRoutes),
    routes.DomainRoute('registry.webintents-org.appspot.com', [
      Route('/<:.*>', handlers_base.PageHandler, 'registry')
    ]),
    routes.DomainRoute('widgets.webintents-org.appspot.com', [
      Route('/<:.*>', widgets.handlers.PageHandler, 'widgets')
    ])
  ])
