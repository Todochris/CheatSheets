# **Cloud-Safe Developer Setup for macOS, Linux, and WSL**

## **1️⃣ Local-only workspace**

Keep all active projects, build artifacts, and temporary files **outside your cloud-synced folders**.

**macOS / Linux / WSL example:**

```
~/Projects/
    MyProject1/
    MyProject2/
~/DevCache/           # caches, build artifacts, venvs, node_modules
```

> All temporary or frequently-changing files stay **local**.

---

## **2️⃣ Cloud-synced folders (Finder/Desktop, OneDrive, Google Drive, etc.)**

* Only store **final deliverables, reports, or zipped releases**.
* Example:

```
~/Documents/LocalProjects/       # symbolic links to local projects
~/Documents/Reports/             # final PDFs, builds, releases
```

---

## **3️⃣ Use symbolic links for convenience**

### macOS / Linux / WSL

```bash
# Link a local project folder to cloud-synced Documents
ln -s ~/Projects/MyProject1 ~/Documents/LocalProjects/MyProject1
```

**Behavior:**

* The symlink appears in the cloud folder.
* Cloud services only see the link itself, **not the project files**.
* You can access the project conveniently without syncing all contents.

> ⚠️ Avoid symlinking folders containing large build artifacts or virtual environments.

---

## **4️⃣ Keep build artifacts, caches, and virtual environments local**

Do not put these in cloud-synced folders:

* `node_modules/`
* `venv/` (Python virtual environments)
* `build/`, `dist/`, `out/` directories

**Tip:** Use `.gitignore` or `.nosync` markers for temporary files.

---

## **5️⃣ Large files and archives**

* Keep ZIPs, datasets, or large downloads in **local-only directories** first:

```
~/Projects/tmp/
```

* Only move to cloud folders if you need to share them.
* Prevents accidental huge uploads.

---

## **6️⃣ Version control best practices**

* Keep Git repositories **outside cloud-synced folders**.
* Commit and push changes normally.
* Avoid syncing `.git` folders to cloud services — thousands of small files can cause massive uploads and slow sync.

---

## **7️⃣ Recommended Folder Structure**

**macOS/Linux/WSL:**

```
~/Projects/               # local projects
~/DevCache/               # temp files, virtualenvs, node_modules
~/Documents/LocalProjects # symbolic links to projects
~/Documents/Reports       # final outputs only
```

**Example symlink command for multiple projects:**

```bash
mkdir -p ~/Documents/LocalProjects
for proj in ~/Projects/*; do
    ln -s "$proj" ~/Documents/LocalProjects/$(basename "$proj")
done
```

* Creates convenient cloud-visible links for all your projects without moving the real data.

---

# **8 Backing up projects + large data**

Version control handles your source code nicely, but **large inputs/outputs** often can’t go in Git. Here’s a strategy:

---

### **Option A: External Backup Drive (Simple & Safe)**

1. Use an external SSD or HDD.
2. Structure it like this:

```
/Volumes/BackupDrive/
    Projects/       # all your source code (optional if you have VCS)
    Data/           # large inputs/outputs
```

3. Use `rsync` (macOS/Linux/WSL) to sync:

```bash
# backup all projects and data to external drive
rsync -avh --progress ~/Projects /Volumes/BackupDrive/Projects
rsync -avh --progress ~/DataBackup /Volumes/BackupDrive/Data
```

* ✅ Efficient (only changes are copied).
* ✅ Works across platforms (WSL, macOS, Linux).
* ✅ Safe for huge files.

---

### **Option B: Cloud Backup for Large Data (Optional)**

* Keep your **real project + data folder local**.
* Use a **cloud service only for archive backups**, not active development.
* Example: `rsync` or `rclone` to OneDrive, Google Drive, or S3-compatible service.

```bash
# example using rclone
rclone copy ~/DataBackup remote:DataBackup --progress
```

* Only uploads data you specify, not all intermediate build artifacts.
* You can schedule incremental backups.

---

### **Option C: Compressed Snapshots**

* For huge datasets that rarely change, consider **zipping or tarballing** them and storing in backup:

```bash
# compress a dataset folder
tar -czvf Dataset_2025-11-10.tar.gz ~/DataBackup/MyBigDataset
# move to external drive or cloud backup
mv Dataset_2025-11-10.tar.gz /Volumes/BackupDrive/Data/
```

* ✅ Keeps number of files small (good for cloud or external drives).
* ✅ Easy to restore with `tar -xzvf`.

---

