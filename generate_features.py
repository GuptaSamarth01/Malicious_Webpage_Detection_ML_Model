import joblib

# Your original feature list (same order used in training)
feature_names = [
    "url_len", "domain_len", "path_len", "num_dots", "contains_ip", "https",
    "has_at_symbol", "has_hyphen", "num_subdirs", "num_params", "num_equals",
    "contains_login", "contains_secure", "contains_bank"
]

# Save it
joblib.dump(feature_names, "feature_names.pkl")
