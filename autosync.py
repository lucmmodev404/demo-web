# auto_sync.py
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AutoGit(FileSystemEventHandler):
    def on_modified(self, event):
        print("🔄 Có thay đổi, kiểm tra commit...")

        # Kiểm tra nếu có gì thay đổi mới commit
        os.system("git add .")
        status = os.popen("git status --porcelain").read()

        if status.strip() != "":
            print("✅ Có thay đổi, đang đẩy lên GitHub...")
            os.system('git commit -m "auto sync"')
            os.system("git push")
        else:
            print("⚠️ Không có gì mới để commit.")

if __name__ == "__main__":
    path = "."  # Thư mục cần theo dõi
    observer = Observer()
    observer.schedule(AutoGit(), path, recursive=True)
    observer.start()
    print("🟢 Đang theo dõi thay đổi... Nhấn Ctrl+C để dừng")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
