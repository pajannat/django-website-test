from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = ""
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = "123456789"
        ctxt["skills"] = [
            "Python",
            "Django",
            "C",
        ]
        ctxt["licenses"] = [
            "基本情報技術者試験",
            "応用情報技術者試験",
            "JDLA Deep Learning for ENGINEER 2021#1",
        ]
        return ctxt
