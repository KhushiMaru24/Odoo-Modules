/** @odoo-module **/
import { Gui } from 'point_of_sale.Gui';
import ProductScreen from 'point_of_sale.ProductScreen';
import ProductItem from 'point_of_sale.ProductItem';
import { PosModel } from 'point_of_sale.models';
import { Registries } from 'point_of_sale.Registries';

// Extend the PosModel to filter unique products
console.log('POS Custom JavaScript loaded');

const ExtendedPosModel = PosModel.extend({
    get_product_list: function () {
        const products = this._super(...arguments); // Use `this._super` to call parent method
        const unique_products = {};
        products.forEach(product => {
            const template_id = product.product_template_id[0];
            if (!unique_products[template_id]) {
                unique_products[template_id] = product;
            }
        });
        return Object.values(unique_products);
    },
});

// Extend the ProductScreen to handle product clicks and show variant selection
class ExtendedProductScreen extends ProductScreen {
    async _onClickProduct(event) {
        const product = event.detail;
        if (product.product_variant_ids.length > 1) {
            Gui.showPopup('SelectionPopup', {
                title: 'Select a Variant',
                list: product.product_variant_ids.map(variant => ({
                    id: variant.id,
                    label: variant.display_name,
                    item: variant,
                })),
                confirm: variant => {
                    this.currentOrder.add_product(this.env.pos.db.get_product_by_id(variant.id));
                },
            });
        } else {
            this.currentOrder.add_product(product);
        }
    }
}

// Extend the ProductItem to display product name
class ExtendedProductItem extends ProductItem {
    get display_name() {
        return this.env.pos.db.get_product_by_id(this.props.product.product_template_id[0]).display_name;
    }
}

// Register the extended classes
Registries.Component.extend(ProductScreen, ExtendedProductScreen);
Registries.Component.extend(ProductItem, ExtendedProductItem);

export { ExtendedPosModel, ExtendedProductScreen, ExtendedProductItem };
