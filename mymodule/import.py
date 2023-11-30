try:
    import mne
except Exception:
    print("Could not import mne, you may have to install (pip install mne)")

raw_array = mne.io.RawArray(data=raw_data, info=info)


