from translations import Translations


translations = Translations()

# Add translations
translations.add_translation("yes", {
    "english": "yes",
    "dutch": "ja",
    "french": "oui"
})
translations.add_translation("no", {
    "english": "no",
    "dutch": "nee",
    "french": "non"
})

# Print translations
print(translations.translations["yes"]["english"])  # Output: "yes"
print(translations.translations["no"]["dutch"])  # Output: "nee"