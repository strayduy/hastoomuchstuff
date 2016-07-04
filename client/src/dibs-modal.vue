<template>
    <ui-modal :show.sync="show_dibs_modal" :header="item.name">

        <ui-textbox label="Name"
                    name="name"
                    :value.sync="username"
                    placeholder="Boaty McBoatface"
                    validation-rules="required"
                    :autocomplete="false"
        ></ui-textbox>

        <ui-textbox label="Comments"
                    name="comments"
                    :value.sync="comments"
                    :multi-line="true"
                    placeholder="(Optional)"
        ></ui-textbox>

        <div slot="footer">
            <template v-if="has_been_claimed">
                <ui-button color="danger" @click="call_dibs" :disabled="!this.can_submit">Send an update</ui-button>
            </template>
            <template v-else>
                <ui-button color="success" @click="call_dibs" :disabled="!this.can_submit">Why yes, I would love to take this off your hands</ui-button>
            </template>
        </div>
    </ui-modal>
</template>

<script>
export default {
    data() {
        return {
            item: {},
            username: '',
            comments: '',
            has_been_claimed: false,
            show_dibs_modal: false,
        };
    },
    computed: {
        can_submit: function() {
            return !!this.username;
        },
    },
    methods: {
        call_dibs: function() {
            if (!this.username) {
                return;
            }

            let data = {
                item: this.item,
                username: this.username,
                comments: this.comments,
            };

            this.$dispatch('claim-item', data);
            this.show_dibs_modal = false;
        },
    },
    events: {
        'dibs-modal.show': function(data) {
            this.item = data.item || {};
            this.comments = '';
            this.has_been_claimed = data.has_been_claimed;
            this.show_dibs_modal = true;
        },
    },
};
</script>
