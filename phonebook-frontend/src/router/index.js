import { createRouter, createWebHistory } from "vue-router";

import ContactList from "../components/ContactList.vue";
import CreateContact from "../components/CreateContact.vue";
import ManageContacts from "../components/ManageContacts.vue";

const routes = [
  { path: "/", component: ContactList },
  { path: "/create", component: CreateContact },
  { path: "/manage", component: ManageContacts },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});