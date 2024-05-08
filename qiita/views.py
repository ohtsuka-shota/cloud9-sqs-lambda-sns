from django.shortcuts import render, redirect
from django.contrib import messages
import boto3
import logging

def file_upload(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if not file:
            messages.error(request, 'No file was selected.')
            return redirect('upload')
        
        # AWS クライアントの設定（環境変数から直接読み込み）
        s3 = boto3.client('s3', region_name='ap-northeast-1')
        
        try:
            # ファイルのアップロード
            s3.upload_fileobj(
                file,
                '●●●',  # S3 バケット名
                file.name
            )
            messages.success(request, 'Upload successfully')
        except Exception as e:
            logging.error(f"Failed to upload to S3: {e}")
            messages.error(request, f'Upload error: {e}')
        
        return redirect('upload')
    
    return render(request, 'upload.html')
