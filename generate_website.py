import os

def generate_website(url):
    page_content = {
        'title': 'PodAnvil - Static Hosting Solution',
        'header': 'Welcome to PodAnvil',
        'main_content': 'We provide cheap, static, secure website hosting solutions in k8s pods.',
        'standard_purchase_text': """
        <div id="paypal-button-container-P-77F74565795170217MTFTRAI"></div>
        <script src="https://www.paypal.com/sdk/js?client-id=sb&vault=true&intent=subscription" data-sdk-integration-source="button-factory"></script>
        <script>
        paypal.Buttons({
            style: {
                shape: 'rect',
                color: 'gold',
                layout: 'vertical',
                label: 'subscribe'
            },
            createSubscription: function(data, actions) {
                return actions.subscription.create({
                'plan_id': 'P-77F74565795170217MTFTRAI'
                });
            },
            onApprove: function(data, actions) {
                alert(data.subscriptionID); // You can add optional success message for the subscriber here
            }
        }).render('#paypal-button-container-P-77F74565795170217MTFTRAI'); // Renders the PayPal button
        </script>
        """,
        'premium_purchase_text': """
        <div id="paypal-button-container-P-97Y90605YR327370YMTFUY7Y"></div>
        <script src="https://www.paypal.com/sdk/js?client-id=sb&vault=true&intent=subscription" data-sdk-integration-source="button-factory"></script>
        <script>
        paypal.Buttons({
            style: {
                shape: 'rect',
                color: 'gold',
                layout: 'vertical',
                label: 'subscribe'
            },
            createSubscription: function(data, actions) {
                return actions.subscription.create({
                'plan_id': 'P-97Y90605YR327370YMTFUY7Y'
                });
            },
            onApprove: function(data, actions) {
                alert(data.subscriptionID); // You can add optional success message for the subscriber here
            }
        }).render('#paypal-button-container-P-97Y90605YR327370YMTFUY7Y'); // Renders the PayPal button
        </script>
        """
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

