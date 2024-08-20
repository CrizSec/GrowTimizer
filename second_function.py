import os
import glob

def delete_files_in_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                results.append(f"Deleted: {file_path}")
            except Exception as e:
                results.append(f"Failed to delete {file_path}: {e}")
    return '\n'.join(results) if results else f'No files to delete in {directory}.'

def delete_log_files_in_appdata(extension='.log'):
    appdata_local = os.getenv('LOCALAPPDATA')
    if not appdata_local:
        return "Tidak dapat menemukan folder AppData\Local."

    search_pattern = os.path.join(appdata_local, '**', '*' + extension)
    log_files = glob.glob(search_pattern, recursive=True)

    if not log_files:
        return f"Tidak ada file dengan ekstensi '{extension}' ditemukan di folder AppData\Local."
    
    for log_file in log_files:
        try:
            os.remove(log_file)
            return f"File {log_file} telah dihapus."
        except Exception as e:
            return f"Gagal menghapus file {log_file}: {e}"