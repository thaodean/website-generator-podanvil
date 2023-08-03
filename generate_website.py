page_content = {
    'title': 'PodAnvil - Static Hosting Solution',
    'header': 'Welcome to PodAnvil',
    'main_content': 'We provide cheap, static, secure website hosting solutions in k8s pods.',
    'standard_purchase_text': """
        <div id="paypal-button-container-Standard"></div>
        <script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID"></script>
        <script>
            paypal.Buttons({
                createOrder: function(data, actions) {
                    // Set up the transaction
                    return actions.order.create({
                        purchase_units: [{
                            amount: {
                                value: '30.00' // Update to match the price of your standard plan
                            }
                        }]
                    });
                }
            }).render('#paypal-button-container-Standard');
        </script>
    """,
    'premium_purchase_text': """
        <div id="paypal-button-container-Premium"></div>
        <script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID"></script>
        <script>
            paypal.Buttons({
                createOrder: function(data, actions) {
                    // Set up the transaction
                    return actions.order.create({
                        purchase_units: [{
                            amount: {
                                value: '70.00' // Update to match the price of your premium plan
                            }
                        }]
                    });
                }
            }).render('#paypal-button-container-Premium');
        </script>
    """
}
