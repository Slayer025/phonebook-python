<template>
  <div class="row justify-content-center mt-5">
    <div class="col-md-6">
      <div class="card p-4 shadow">
        <h3 class="mb-3 text-center">Create Contact</h3>

        <form @submit.prevent="create">
          <div class="mb-3">
            <label class="form-label">Name</label>
            <input v-model="form.name" class="form-control" placeholder="John Doe" />
            <small class="text-danger" v-if="errors.name">{{ errors.name }}</small>
          </div>

          <div class="mb-3">
            <label class="form-label">Phone</label>
            <input v-model="form.phone_number" class="form-control" placeholder="+1234567890" />
            <small class="text-danger" v-if="errors.phone">{{ errors.phone }}</small>
          </div>

          <div class="mb-3">
            <label class="form-label">Email (Optional)</label>
            <input v-model="form.email" class="form-control" placeholder="email@example.com" />
            <small class="text-danger" v-if="errors.email">{{ errors.email }}</small>
          </div>

          <div class="mb-3">
            <label class="form-label">Address (Optional)</label>
            <input v-model="form.address" class="form-control" placeholder="123 Street Ave" />
          </div>

          <button class="btn btn-success w-100 shadow-sm">Save Contact</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  data() {
    return {
      form: {
        name: "",
        phone_number: "",
        email: "",
        address: "",
      },
      errors: {},
    };
  },
  methods: {
    validate() {
      this.errors = {};
      const nameRegex = /^[A-Za-z\s]+$/;
      
      if (!this.form.name) {
        this.errors.name = "Name is required";
      } else if (!nameRegex.test(this.form.name)) {
        this.errors.name = "Only letters allowed";
      }

      const phoneRegex = /^\+?\d{10,15}$/;
      if (!phoneRegex.test(this.form.phone_number)) {
        this.errors.phone = "Invalid phone number (10-15 digits)";
      }

      if (this.form.email && this.form.email.trim() !== "") {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(this.form.email)) {
          this.errors.email = "Invalid email format";
        }
      }

      return Object.keys(this.errors).length === 0;
    },

    async create() {
      if (!this.validate()) return;

      // CLEAN DATA: Convert empty strings to null for the database
      const payload = {
        name: this.form.name.trim(),
        phone_number: this.form.phone_number.trim(),
        email: this.form.email?.trim() || null,
        address: this.form.address?.trim() || null
      };

      try {
        await api.post("/contacts/", payload);
        alert("Contact created successfully!");
        this.$router.push("/");
      } catch (err) {
        const msg = err.response?.data?.detail || "Error creating contact";
        alert(msg);
      }
    },
  },
};
</script>