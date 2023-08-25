conda run --live-stream -n WavJourney python -u services.py 2>&1 | tee services_logs/service.out &
conda run --live-stream -n WavJourney python -u ui_client.py 2>&1 | tee services_logs/wavejourney.out