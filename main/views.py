import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import DocumentForm
from .models import Document
from docx2pdf import convert

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            input_path = document.upload.path
            output_path = os.path.splitext(input_path)[0] + '.pdf'
            try:
                convert(input_path, output_path)
                with open(output_path, 'rb') as pdf_file:
                    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                    response['Content-Disposition'] = f'attachment; filename={os.path.basename(output_path)}'
                    return response
            except Exception as e:
                form.add_error(None, f"Error converting document: {e}")
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})
