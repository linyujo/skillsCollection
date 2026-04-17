import os
import requests
import yaml
import sys

def download_raw_github_file(repo, branch, file_path, local_dest):
    """
    從 GitHub Raw 下載單一檔案
    """
    raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{file_path}"
    
    try:
        response = requests.get(raw_url, timeout=10)
        # 檢查請求是否成功
        if response.status_code == 200:
            # 確保本地資料夾存在
            os.makedirs(os.path.dirname(local_dest), exist_ok=True)
            
            with open(local_dest, "wb") as f:
                f.write(response.content)
            print(f"✅ 成功同步: {repo} -> {local_dest}")
        else:
            print(f"❌ 下載失敗: {repo}/{file_path} (狀態碼: {response.status_code})")
    except Exception as e:
        print(f"⚠️ 發生錯誤: {e}")

def main():
    config_file = "skills_config.yaml"
    
    if not os.path.exists(config_file):
        print(f"錯誤: 找不到設定檔 {config_file}")
        sys.exit(1)

    with open(config_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if not config or "sources" not in config:
        print("錯誤: 設定檔格式不正確")
        sys.exit(1)

    print("🚀 開始同步 Agent Skills...")
    
    for source in config["sources"]:
        repo = source.get("repo")
        branch = source.get("branch", "main") # 預設為 main
        files = source.get("files", [])
        dest_dir = source.get("dest", "")
        
        for source_path in files:
            file_name = os.path.basename(source_path)
            dest_path = os.path.join(dest_dir, file_name)
            download_raw_github_file(repo, branch, source_path, dest_path)

    print("\n✨ 同步任務完成！")

if __name__ == "__main__":
    main()