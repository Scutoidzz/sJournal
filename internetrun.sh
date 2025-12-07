#/bin/bash
echo "The installation will start in 10 seconds. Press Ctrl+C to cancel."
sleep 10
echo "Downloading sJournal"
git clone https://github.com/scutoid/sJournal.git
cd sJournal
echo "Installing pip dependencies"
pip install -r requirements.txt --break-system-packages
echo "Downloaded. Running app"
echo "..."
sleep 1
python main.py
