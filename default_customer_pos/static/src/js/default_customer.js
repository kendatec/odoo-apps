odoo.define('default_customer_pos.model', function(require) {
    "use strict";

    var models = require('point_of_sale.models');
    models.load_fields('pos.config', ['customer_default_id']);
    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
        initialize: function(attributes, options) {
            _super_order.initialize.call(this, attributes, options);
            if (this.pos.config.customer_default_id && !this.get_client()) {
                var customer_default = this.pos.config.customer_default_id;
                if (customer_default) {
                    var client = this.pos.db.get_partner_by_id(customer_default[0]);
                    if (client) {
                        this.set_client(client);
                    }
                }
            }
        },
    });
});