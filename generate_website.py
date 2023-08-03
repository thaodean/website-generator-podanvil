#!/usr/bin/env python3
import os

def generate_website(url):
    page_content = {
        'title': 'PodAnvil - Static Hosting Solution',
        'header': 'Welcome to PodAnvil',
        'main_content': 'We provide cheap, static, secure website hosting solutions in k8s pods.',
        'premium_purchase_link': 'https://payment-gateway.com/podanvil',
        'premium_purchase_text': """<div id="paypal-button-container-Premium"></div>""",
        'standard_purchase_link': 'https://payment-gateway.com/podanvil',
        'standard_purchase_text': """<div id="paypal-button-container-Standard"></div>""",
    }

    with open('index.html.template', 'r') as file:
        template = file.read()

    for placeholder, value in page_content.items():
        template = template.replace(f'{{{{ {placeholder} }}}}', value)

    new_dir_path = os.path.join(os.getcwd(), url)
    os.makedirs(new_dir_path, exist_ok=True)

    with open(os.path.join(new_dir_path, 'index.html'), 'w') as file:
        file.write(template)

    print("Website successfully generated!")

generate_website('podanvil.com')
