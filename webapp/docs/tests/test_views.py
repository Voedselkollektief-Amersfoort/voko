from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse
from docs.tests.factories import DocumentFactory
from vokou.testing import VokoTestCase


class TestDocumentOverview(VokoTestCase):
    def setUp(self):
        self.url = reverse('docs.document_overview')
        self.login()

    def test_login_required(self):
        self.logout()
        ret = self.client.get(self.url)
        self.assertEqual(ret.status_code, 302)

    def test_context_data(self):
        docs = DocumentFactory.create_batch(5)
        ret = self.client.get(self.url)
        self.assertItemsEqual(ret.context['object_list'], docs)


class TestDocumentDownload(VokoTestCase):
    def setUp(self):
        self.tmpfile = SimpleUploadedFile('filename.pdf', 'file contents')
        self.doc = DocumentFactory(file=self.tmpfile)
        self.url = reverse('docs.document_download', args=(self.doc.slug, ))
        self.login()

    def test_login_required(self):
        self.logout()
        ret = self.client.get(self.url)
        self.assertEqual(ret.status_code, 302)

    def test_response(self):
        ret = self.client.get(self.url)
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.content, "file contents")
        self.assertEqual(ret['content-type'], "application/octet-stream")
        # self.assertEqual(ret['content-disposition'], "attachment; filename=%s" % ?)
