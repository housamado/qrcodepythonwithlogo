import segno

def generate_qr_code(data, filename):
    """Créer le QR code avec les données fournies et l'enregistrer sous forme d'image."""
    qr = segno.make(data)  # Créer le QR code
    qr.save(filename)      # Enregistrer le QR code comme image

# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez par vos données professionnelles
    name = "Votre Nom"
    title = "Votre Titre"
    company = "Nom de l'Entreprise"
    phone = "+33 1 23 45 67 89"  # Exemple de numéro de téléphone
    email = "votre.email@entreprise.com"
    website = "https://www.entreprise.com"
    
    # Créez une chaîne de données à encoder dans le QR code
    data_to_encode = f"""
    Nom: {name}
    Titre: {title}
    Entreprise: {company}
    Téléphone: {phone}
    Email: {email}
    Site Web: {website}
    """
    
    output_filename = "qr_code.png"  # Nom du fichier de sortie
    generate_qr_code(data_to_encode.strip(), output_filename)
