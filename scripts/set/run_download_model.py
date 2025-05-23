from huggingface_hub import snapshot_download
import os


if __name__ == "__main__":
    CKPT_DIR = os.environ['CKPT_DIR']

    print("Downloading Qwen/Qwen3-0.6B-Base ...")
    snapshot_download(repo_id="Qwen/Qwen3-0.6B-Base",
                      local_dir=f"{CKPT_DIR}/models/Qwen3-0.6B-Base/base")
