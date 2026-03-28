<template>
  <div class="container mt-4">
    

    <div class="input-group mb-3 shadow-sm">
      <span class="input-group-text bg-white"><i class="bi bi-search"></i></span>
      <input 
        class="form-control" 
        v-model="search" 
        placeholder="Search by name, phone, email, or address..." 
        @input="page = 1" 
      />
    </div>

    <div class="table-responsive shadow-sm">
      <table class="table table-hover table-bordered align-middle bg-white">
        <thead class="table-dark">
          <tr>
            <th>Name</th>
            <th>Phone</th>
            <th>Email</th>
            <th>Address</th>
            <th class="text-center">Actions</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="c in paginated" :key="c.id">
            <td><input v-model="c.name" class="form-control form-control-sm" /></td>
            <td><input v-model="c.phone_number" class="form-control form-control-sm" /></td>
            <td><input v-model="c.email" class="form-control form-control-sm"  /></td>
            <td><input v-model="c.address" class="form-control form-control-sm"  /></td>

            <td class="text-center">
              <button class="btn btn-warning btn-sm me-1" @click="update(c)">Update</button>
              <button class="btn btn-danger btn-sm" @click="remove(c.id)">Delete</button>
            </td>
          </tr>
          <tr v-if="filtered.length === 0">
            <td colspan="5" class="text-center py-4 text-muted">No contacts found matching your search.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="d-flex justify-content-between align-items-center mt-3">
      <button class="btn btn-outline-secondary btn-sm" @click="prev" :disabled="page === 1">Prev</button>
      <span class="text-muted">Page {{ page }} of {{ totalPages }}</span>
      <button class="btn btn-outline-secondary btn-sm" @click="next" :disabled="page === totalPages">Next</button>
    </div>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  data() {
    return {
      contacts: [],
      search: "",
      page: 1,
      size: 5,
    };
  },
  computed: {
    filtered() {
      const query = this.search.toLowerCase().trim();
      if (!query) return this.contacts;

      return this.contacts.filter((c) => {
        // Search through all fields, handling null values safely
        return (
          (c.name || "").toLowerCase().includes(query) ||
          (c.phone_number || "").toLowerCase().includes(query) ||
          (c.email || "").toLowerCase().includes(query) ||
          (c.address || "").toLowerCase().includes(query)
        );
      });
    },
    totalPages() {
      return Math.ceil(this.filtered.length / this.size) || 1;
    },
    paginated() {
      const start = (this.page - 1) * this.size;
      return this.filtered.slice(start, start + this.size);
    },
  },
  methods: {
    validate(c) {
      const nameRegex = /^[A-Za-z\s]+$/;
      const phoneRegex = /^\+?\d{10,15}$/;

      if (!c.name || !nameRegex.test(c.name)) {
        alert("Name is required and must only contain letters.");
        return false;
      }
      if (!c.phone_number || !phoneRegex.test(c.phone_number)) {
        alert("A valid phone number is required.");
        return false;
      }
      if (c.email && c.email.trim() !== "") {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(c.email)) {
          alert("Invalid email format.");
          return false;
        }
      }
      return true;
    },

    async update(c) {
      if (!this.validate(c)) return;

      // Prepare payload to handle optional fields
      const payload = {
        name: c.name.trim(),
        phone_number: c.phone_number.trim(),
        email: (c.email && c.email.trim()) ? c.email.trim() : null,
        address: (c.address && c.address.trim()) ? c.address.trim() : null
      };

      try {
        await api.put(`/contacts/${c.id}`, payload);
        alert("Updated!");
      } catch (err) {
        alert(err.response?.data?.detail || "Update failed");
      }
    },

    async remove(id) {
      if (!confirm("Are you sure?")) return;
      try {
        await api.delete(`/contacts/${id}`);
        this.contacts = this.contacts.filter((c) => c.id !== id);
        if (this.paginated.length === 0 && this.page > 1) this.page--;
      } catch (err) {
        alert("Delete failed");
      }
    },

    next() { if (this.page < this.totalPages) this.page++; },
    prev() { if (this.page > 1) this.page--; },
  },
  async mounted() {
    try {
      const res = await api.get("/contacts/");
      this.contacts = res.data;
    } catch (e) { console.error(e); }
  },
};
</script>