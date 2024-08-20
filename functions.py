import os
import tempfile
import glob
from second_function import delete_files_in_directory, delete_log_files_in_appdata

def delete_temp_files(ui):
    if ui.tempFiles.isChecked():
        temp_dir = tempfile.gettempdir()
        results = []
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    results.append(f'Deleted: {file_path}')
                except Exception as e:
                    results.append(f'Failed to delete: {file_path}: {e}')
        return '\n'.join(results) if results else 'No temp files to delete.'
    return 'Temp files option not selected.'

def delete_system_temp(ui):
    if ui.systemTemp.isChecked():
        results = []
        system_temp_dirs = [
            os.path.join(os.getenv('SystemRoot'), 'Temp'),
            '/var/tmp',
            '/tmp'
        ]
        for dir_path in system_temp_dirs:
            if os.path.exists(dir_path):
                result = delete_files_in_directory(dir_path)
                results.append(result)
        return '\n'.join(results) if results else 'No system temp files to delete.'
    return 'System temp option not selected.'

def delete_prefetch_files(ui):
    if ui.prefetch.isChecked():
        prefetch_dir = os.path.join(os.getenv('SystemRoot'), 'Prefetch')
        
        if os.path.exists(prefetch_dir):
            return delete_files_in_directory(prefetch_dir)
        else:
            return f"Prefetch directory not found: {prefetch_dir}"
    return 'Prefetch option not selected.'

def app_logs(ui):
    if ui.appLogs.isChecked():
        return 'App logs cleaned successfully...'
    return 'App logs option not selected.'

def log_files(ui):
    if ui.logFiles.isChecked():
        result = delete_log_files_in_appdata(extension='.log')
        return result
    return 'Log files option not selected.'

def update_logs(ui):
    if ui.updateLogs.isChecked():
        update_logs_extension = '.update.log'
        appdata_local = os.getenv('LOCALAPPDATA')
        if appdata_local:
            search_pattern = os.path.join(appdata_local, '**', '*' + update_logs_extension)
            update_log_files = glob.glob(search_pattern, recursive=True)
            
            if not update_log_files:
                return f"Tidak ada file dengan ekstensi '{update_logs_extension}' ditemukan di folder AppData\Local."
            
            results = []
            for log_file in update_log_files:
                try:
                    os.remove(log_file)
                    results.append(f"File {log_file} telah dihapus.")
                except Exception as e:
                    results.append(f"Gagal menghapus file {log_file}: {e}")
            return '\n'.join(results) if results else 'No update logs to delete.'
        return 'Folder AppData\Local tidak ditemukan.'
    return 'Update logs option not selected.'
