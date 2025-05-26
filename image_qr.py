import segno
from PIL import Image

def generate_qr_code_with_logo(data, logo_path, output_filename):
    """Créer un code QR avec un logo au centre et l'enregistrer sous forme d'image."""
    # Générer le code QR avec haute correction d'erreur
    qr = segno.make(data, error='H')

    # Enregistrer le code QR avec des options de style
    qr.save('temp_qr_code.png', scale=10, dark='#282C63', light='#FFFFFF')  # Couleur interne des yeux et fond blanc

    # Ouvrir l'image du code QR enregistrée
    qr_image = Image.open('temp_qr_code.png').convert("RGBA")  # Assurez-vous que le QR est en mode RGBA

    # Ouvrir l'image du logo
    logo = Image.open(logo_path).convert("RGBA")  # Gardez le logo en mode RGBA

    # Calculer la taille du logo (25% de la taille du code QR)
    qr_width, qr_height = qr_image.size
    logo_size = int(qr_width * 0.25)  # Ajustez la taille si nécessaire
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)  # Utilisez LANCZOS pour une haute qualité

    # Créer une bordure blanche autour du logo
    border_size = 10  # Taille de la bordure blanche
    bordered_logo_size = logo_size + 2 * border_size  # Taille totale avec la bordure
    bordered_logo = Image.new('RGBA', (bordered_logo_size, bordered_logo_size), (255, 255, 255, 255))  # Fond blanc

    # Coller le logo au centre de la bordure blanche
    bordered_logo.paste(logo, (border_size, border_size), mask=logo)  # Utiliser le logo comme masque pour conserver la transparence

    # Calculer la position pour centrer le logo avec bordure
    position = ((qr_width - bordered_logo_size) // 2, (qr_height - bordered_logo_size) // 2)

    # Créer une nouvelle image pour la sortie finale
    final_image = Image.new('RGBA', qr_image.size)

    # Coller le code QR sur l'image finale
    final_image.paste(qr_image, (0, 0))

    # Coller le logo avec bordure sur l'image finale
    final_image.paste(bordered_logo, position)

    # Enregistrer l'image finale avec le code QR et le logo centré
    final_image.save(output_filename)

# Exemple d'utilisation
if __name__ == "__main__":
    name = "Votre Nom"
    title = "Votre Titre"
    company = "Nom de l'Entreprise"
    phone = "+33 1 23 45 67 89"  # Exemple de numéro de téléphone
    email = "votre.email@entreprise.com"
    website = "https://www.entreprise.com"

    # Créer le contenu du code QR
    data_to_encode = (
        f"Nom: {name}\n"
        f"Titre: {title}\n"
        f"Entreprise: {company}\n"
        f"Téléphone: {phone}\n"
        f"Email: {email}\n"
        f"Site Web: {website}"
    )

    logo_path = "bouquet_cake.png"          # Chemin vers votre fichier logo
    output_filename = "qr_code_with_logo.png"   # Nom de fichier de sortie pour le code QR

    generate_qr_code_with_logo(data_to_encode, logo_path, output_filename)
