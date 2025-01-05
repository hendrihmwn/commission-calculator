<template>
    <div class="container">
      <div class="row">
        <div class="row mb-2">
            <p class="col h5">
                List of Sales Data
            </p>
            <div class="col">
                <div class="float-end">
                    <button
                        type="button"
                        class="btn btn-success btn-sm"
                        @click="toggleAddSalesModal">
                        Add Sales
                    </button>
                    <button
                        type="button"
                        class="btn btn-success btn-sm ms-2"
                        @click="toggleAddFileModal">
                        Add from Excel File
                    </button>
                    <button
                        type="button"
                        class="btn btn-danger btn-sm ms-2"
                        @click="handleAddReset">
                        Reset
                    </button>
                </div>
            </div>
          
        </div>
            
            <div class="table-overflow mb-2 shadow-sm mb-2 bg-body rounded">
                <table class="table table-bordered table-striped">
                    <thead>
                        <tr>
                        <th class="fw-bolder">SO</th>
                        <th class="fw-bolder">SP</th>
                        <th class="fw-bolder">SM</th>
                        <th class="fw-bolder">GM</th>
                        <th class="fw-bolder">Item</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-if="sales.length == 0">
                            <td colspan="5">No sales data</td>
                        </tr>
                        <tr v-for="sale in sales">
                            <td>{{ sale.so }}</td>
                            <td>{{ sale.sp }}</td>
                            <td>{{ sale.sm }}</td>
                            <td>{{ sale.gm }}</td>
                            <td>{{ sale.item }}</td>
                        </tr>
                        
                    </tbody>
                </table>
            </div>
            <p class="mb-3">Total Data: {{ sales.length }}</p>
          <div class="row justify-content-md-center">
                
                <div class="col-md-auto">
                    <button
                        type="button"
                        class="btn btn-primary btn-md ms-2"
                        @click="calculateIncentive">
                        Calculate Commission
                    </button>
                </div>
            </div>
      </div>

      <br /><br />

      <div v-show="activeCalculation" class="row">
        <h4 class="col-md-8">
            SP Commission Table
        </h4>
        <div class="table-overflow mb-2 shadow-sm bg-body rounded mb-5">
            <table class="table table-bordered table-hover">
                <thead class="table-light fw-bolder">
                    <tr>
                        <th class="align-middle text-center" rowspan="2">Name</th>
                        <th class="align-middle text-center table-danger" colspan="3">Red Commission</th>
                        <th class="align-middle text-center table-primary" colspan="3">Blue Commission</th>
                        <th class="align-middle text-center table-warning" colspan="3">Yellow Commission</th>
                        <th class="align-middle text-center" rowspan="2">Basic Commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="red commission + blue commission + yellow commission">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                        <th class="align-middle text-center" rowspan="2">Total Sales Point</th>
                        <th class="align-middle text-center" rowspan="2">Performance Incentive</th>
                        <th class="align-middle text-center" rowspan="2">Total Commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="basic commission + performance incentive">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                    </tr>
                    <tr>
                        <th class="table-danger align-middle text-center" scope="col">sales point</th>
                        <th class="table-danger align-middle text-center" scope="col">commision point</th>
                        <th class="table-danger align-middle text-center" scope="col">commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="Rp 7.500 x red commission point / 100">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                        <th class="table-primary align-middle text-center" scope="col">sales point</th>
                        <th class="table-primary align-middle text-center" scope="col">commision point</th>
                        <th class="table-primary align-middle text-center" scope="col">commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="Rp 10.000 x blue commission point / 100">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                        <th class="table-warning align-middle text-center" scope="col">sales point</th>
                        <th class="table-warning align-middle text-center" scope="col">commision point</th>
                        <th class="table-warning align-middle text-center" scope="col">commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="Rp 25.000 x yellow commission point / 100">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="sp in commission_sp">
                        <td>{{ sp.name }}</td>
                        <td class="text-end table-danger">{{ sp.red_total_sales_point }}</td>
                        <td class="text-end table-danger">{{ sp.red_commission_point }}</td>
                        <td class="text-end table-danger">{{ sp.red_basic_commission }}</td>
                        <td class="text-end table-primary">{{ sp.blue_total_sales_point }}</td>
                        <td class="text-end table-primary">{{ sp.blue_commission_point }}</td>
                        <td class="text-end table-primary">{{ sp.blue_basic_commission }}</td>
                        <td class="text-end table-warning">{{ sp.yellow_total_sales_point }}</td>
                        <td class="text-end table-warning">{{ sp.yellow_commission_point }}</td>
                        <td class="text-end table-warning">{{ sp.yellow_basic_commission }}</td>
                        <td class="text-end">{{ sp.basic_commission }}</td>
                        <td class="text-end">{{ sp.total_sales_point }}</td>
                        <td class="text-end">{{ sp.performance_incentive }}</td>
                        <td class="text-end">{{ sp.total_commission }}</td>
                    </tr>
                </tbody>
                
            </table>
        </div>

        <h4 class="col-md-8">
            SM Commission Table
        </h4>
        <div class="table-overflow mb-2 shadow-sm bg-body rounded mb-5">
            <table class="table table-bordered table-hover">
                <thead class="table-light fw-bolder">
                    <tr>
                        <th class="align-middle text-center" rowspan="2">Name</th>
                        <th class="align-middle text-center table-danger" colspan="3">Red Commission</th>
                        <th class="align-middle text-center table-primary" colspan="3">Blue Commission</th>
                        <th class="align-middle text-center table-warning" colspan="3">Yellow Commission</th>
                        <th class="align-middle text-center" rowspan="2">Basic Commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="red commission + blue commission + yellow commission">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                        <th class="align-middle text-center" rowspan="2">Total Sales Point</th>
                        <th class="align-middle text-center" rowspan="2">Total Active SP</th>
                        <th class="align-middle text-center" rowspan="2">Performance Incentive</th>
                        <th class="align-middle text-center" rowspan="2">Total Commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="basic commission + performance incentive">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                    </tr>
                    <tr>
                        <th class="table-danger align-middle text-center" scope="col">sales point</th>
                        <th class="table-danger align-middle text-center" scope="col">commision point</th>
                        <th class="table-danger align-middle text-center" scope="col">commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="Rp 7.500 x red commission point / 100">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                        <th class="table-primary align-middle text-center" scope="col">sales point</th>
                        <th class="table-primary align-middle text-center" scope="col">commision point</th>
                        <th class="table-primary align-middle text-center" scope="col">commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="Rp 10.000 x blue commission point / 100">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                        <th class="table-warning align-middle text-center" scope="col">sales point</th>
                        <th class="table-warning align-middle text-center" scope="col">commision point</th>
                        <th class="table-warning align-middle text-center" scope="col">commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="Rp 25.000 x yellow commission point / 100">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="sm in commission_sm">
                        <td>{{ sm.name }}</td>
                        <td class="text-end table-danger">{{ sm.red_total_sales_point }}</td>
                        <td class="text-end table-danger">{{ sm.red_commission_point }}</td>
                        <td class="text-end table-danger">{{ sm.red_basic_commission }}</td>
                        <td class="text-end table-primary">{{ sm.blue_total_sales_point }}</td>
                        <td class="text-end table-primary">{{ sm.blue_commission_point }}</td>
                        <td class="text-end table-primary">{{ sm.blue_basic_commission }}</td>
                        <td class="text-end table-warning">{{ sm.yellow_total_sales_point }}</td>
                        <td class="text-end table-warning">{{ sm.yellow_commission_point }}</td>
                        <td class="text-end table-warning">{{ sm.yellow_basic_commission }}</td>
                        <td class="text-end">{{ sm.basic_commission }}</td>
                        <td class="text-end">{{ sm.total_sales_point }}</td>
                        <td class="text-end">{{ sm.total_active_sp }}</td>
                        <td class="text-end">{{ sm.performance_incentive }}</td>
                        <td class="text-end">{{ sm.total_commission }}</td>
                    </tr>
                </tbody>
                
            </table>
        </div>

        <h4 class="col-md-8">
            GM Commission Table
        </h4>
        <div class="table-overflow mb-2 shadow-sm bg-body rounded">
            <table class="table table-bordered table-hover">
                <thead class="table-light fw-bolder">
                    <tr>
                        <th class="align-middle text-center" rowspan="2">Name</th>
                        <th class="align-middle text-center table-danger" colspan="3">Red Commission</th>
                        <th class="align-middle text-center table-primary" colspan="3">Blue Commission</th>
                        <th class="align-middle text-center table-warning" colspan="3">Yellow Commission</th>
                        <th class="align-middle text-center" rowspan="2">Basic Commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="red commission + blue commission + yellow commission">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                        <th class="align-middle text-center" rowspan="2">Total Sales Point</th>
                        <th class="align-middle text-center" rowspan="2">Total Active SM</th>
                        <th class="align-middle text-center" rowspan="2">Performance Incentive</th>
                        <th class="align-middle text-center" rowspan="2">Total Commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="basic commission + performance incentive">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                    </tr>
                    <tr>
                        <th class="table-danger align-middle text-center" scope="col">sales point</th>
                        <th class="table-danger align-middle text-center" scope="col">commision point</th>
                        <th class="table-danger align-middle text-center" scope="col">commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="Rp 7.500 x red commission point / 100">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                        <th class="table-primary align-middle text-center" scope="col">sales point</th>
                        <th class="table-primary align-middle text-center" scope="col">commision point</th>
                        <th class="table-primary align-middle text-center" scope="col">commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="Rp 10.000 x blue commission point / 100">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                        <th class="table-warning align-middle text-center" scope="col">sales point</th>
                        <th class="table-warning align-middle text-center" scope="col">commision point</th>
                        <th class="table-warning align-middle text-center" scope="col">commission
                            <p class="align-top" data-toggle="tooltip" data-placement="top" title="Rp 25.000 x yellow commission point / 100">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-info-circle-fill" viewBox="0 0 16 16">
                                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"></path>
                                </svg>
                            </p>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="gm in commission_gm">
                        <td>{{ gm.name }}</td>
                        <td class="text-end table-danger">{{ gm.red_total_sales_point }}</td>
                        <td class="text-end table-danger">{{ gm.red_commission_point }}</td>
                        <td class="text-end table-danger">{{ gm.red_basic_commission }}</td>
                        <td class="text-end table-primary">{{ gm.blue_total_sales_point }}</td>
                        <td class="text-end table-primary">{{ gm.blue_commission_point }}</td>
                        <td class="text-end table-primary">{{ gm.blue_basic_commission }}</td>
                        <td class="text-end table-warning">{{ gm.yellow_total_sales_point }}</td>
                        <td class="text-end table-warning">{{ gm.yellow_commission_point }}</td>
                        <td class="text-end table-warning">{{ gm.yellow_basic_commission }}</td>
                        <td class="text-end">{{ gm.basic_commission }}</td>
                        <td class="text-end">{{ gm.total_sales_point }}</td>
                        <td class="text-end">{{ gm.total_active_sm }}</td>
                        <td class="text-end">{{ gm.performance_incentive }}</td>
                        <td class="text-end">{{ gm.total_commission }}</td>
                    </tr>
                </tbody>
                
            </table>
        </div>
    </div>
  
      <!-- add new sales modal -->
      <div
        ref="addSalesModal"
        class="modal fade"
        :class="{ show: activeAddSalesModal, 'd-block': activeAddSalesModal }"
        tabindex="-1"
        role="dialog">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Add a new sales</h5>
            </div>
            <div class="modal-body">
                <p class="text-danger" v-show="showError">All field required</p>
              <form>
                <div class="mb-3">
                  <label for="addSalesSO" class="form-label">SO:<span class="text-danger align-top">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    id="addSalesSO"
                    v-model="addSalesForm.so"
                    placeholder="Enter SO">
                </div>
                <div class="mb-3">
                  <label for="addSalesSP" class="form-label">SP:<span class="text-danger align-top">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    id="addSalesSP"
                    v-model="addSalesForm.sp"
                    placeholder="Enter SP">
                </div>
                <div class="mb-3">
                  <label for="addSalesSM" class="form-label">SM:<span class="text-danger align-top">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    id="addSalesSM"
                    v-model="addSalesForm.sm"
                    placeholder="Enter SM">
                </div>
                <div class="mb-3">
                  <label for="addSalesGM" class="form-label">GM:<span class="text-danger align-top">*</span></label>
                  <input
                    type="text"
                    class="form-control"
                    id="addSalesGM"
                    v-model="addSalesForm.gm"
                    placeholder="Enter GM">
                </div>
                <div class="mb-3">
                  <label for="addSalesItem" class="form-label">Item:<span class="text-danger align-top">*</span></label>
                  <select
                    class="form-control"
                    id="addSalesItem"
                    v-model="addSalesForm.item"
                    placeholder="Select Item">
                    <option v-for="item in items" :value="item">{{ item }}</option>
                  </select>
                </div>
                <button
                    type="button"
                    class="btn btn-primary btn-sm col-md-2"
                    @click="handleAddSubmit">
                    Add
                  </button>
                  <button
                    type="button"
                    class="btn btn-default btn-sm col-md-2 ml-5"
                    @click="toggleAddSalesModal">
                    Cancel
                  </button>
              </form>
            </div>
          </div>
        </div>
      </div>
      <div v-if="activeAddSalesModal" class="modal-backdrop fade show"></div>

      <!-- add file modal -->
      <div
        ref="addFileModal"
        class="modal fade"
        :class="{ show: activeAddFileModal, 'd-block': activeAddFileModal }"
        tabindex="-1"
        role="dialog">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Add from Excel File</h5>
              <button
                type="button"
                class="btn btn-default btn-sm ms-2 float-end"
                @click="downloadTemplate">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cloud-arrow-down" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M7.646 10.854a.5.5 0 0 0 .708 0l2-2a.5.5 0 0 0-.708-.708L8.5 9.293V5.5a.5.5 0 0 0-1 0v3.793L6.354 8.146a.5.5 0 1 0-.708.708z"></path>
                <path d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383m.653.757c-.757.653-1.153 1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1 10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15 9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"></path>
                </svg>Template Format
            </button>
            </div>
            <div class="modal-body">
                <p class="text-danger" v-show="showErrorFile">Wrong Template or Format</p>
                <form @submit.prevent="uploadFile">
                    <div class="mb-3">
                        <label for="uploadFile" class="form-label">File:<span class="text-danger align-top">*</span></label>
                        <input
                        type="file"
                        class="form-control"
                        id="uploadFile"
                        @change="onFileChange" 
                        accept=".xls,.xlsx"
                        placeholder="Enter title">
                    </div>
                    <div class="btn-group" role="group">
                        <button
                        type="submit"
                        class="btn btn-primary btn-sm"
                        :disabled="!file">
                        Submit
                        </button>
                    </div>
                    <button
                        type="button"
                        class="btn btn-default btn-sm col-md-2 ml-5"
                        @click="toggleAddFileModal">
                        Cancel
                    </button>
                </form>
            </div>
          </div>
        </div>
      </div>
      <div v-if="activeAddFileModal" class="modal-backdrop fade show"></div>
  
    </div>
  </template>
  
  <style>
    .table-overflow{   
        max-height: 400px !important;
        overflow: scroll;
    }
    thead {
        position: sticky;
        top: 0;
        z-index: 2;
        border-bottom: solid 1px;
    }
    .red{
        background-color: red !important;
    }
    .blue{
        background-color: blue !important;
    }
    .yellow{
        background-color: yellow !important;

    }
    
  </style>
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        backendHost: import.meta.env.VITE_BACKEND_HOST,
        message: '',
        showMessage: false,
        file: null,
        uploadStatus: "",
        addSalesForm: {
          so: '',
          sp: '',
          sm: '',
          gm: '',
          item: ''
        },
        activeAddSalesModal: false,
        activeAddFileModal: false,
        activeCalculation: false,
        sales: [],
        items: ['red', 'blue', 'yellow'],
        commission_sp: [],
        commission_sm: [],
        commission_gm: [],
        showError: false,
        showErrorFile: false
      };
    },
    methods: {
        async downloadTemplate() {
            try {
                const response = await axios.get(this.backendHost+"/sample_data.xlsx", { responseType: "blob" });
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement("a");
                link.href = url;
                link.setAttribute("download", "sample.xlsx");
                document.body.appendChild(link);
                link.click();
                link.remove();
            } catch (error) {
                console.error("Error downloading file:", error);
            }
        },
        onFileChange(event) {
            this.file = event.target.files[0]; // Get the selected file
        },
        async uploadFile() {
            if (!this.file) {
                this.uploadStatus = "Please select a file first.";
                return;
            }
            const formData = new FormData();
            formData.append("file", this.file);
            try {
                const response = await axios.post(this.backendHost+"/read-file", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
                });
                // console.log(response.data.data);
                for(var key in response.data.data) {
                    this.sales.push(response.data.data[key]);
                }
                this.toggleAddFileModal();
            } catch (error) {
                console.error(error);
                this.showErrorFile = true
            }
        },
      handleFileUpload() {
        const payload = {
          file: this.fileUploadForm.file
        };
        this.uploadFile(payload);
      },
      handleAddReset() {
        this.initForm();
        this.sales = [];
        this.commission_sp = [];
        this.commission_sm = [];
        this.commission_gm = [];
        this.activeCalculation = false;
      },
      handleAddSubmit() {
        if(this.addSalesForm.so == "" || this.addSalesForm.sp == "" || this.addSalesForm.sm == "" || this.addSalesForm.gm == "" || this.addSalesForm.item == ""){
            console.log("mampir");
            this.showError = true;
            return;
        }
        this.toggleAddSalesModal();
        
        this.sales.push({
            so: this.addSalesForm.so,
            sp: this.addSalesForm.sp,
            sm: this.addSalesForm.sm,
            gm: this.addSalesForm.gm,
            item: this.addSalesForm.item,
        });
        this.initForm();
      },
      initForm() {
        this.addSalesForm.so = '';
        this.addSalesForm.sp = '';
        this.addSalesForm.sm = '';
        this.addSalesForm.gm = '';
        this.addSalesForm.item = '';
        this.showError = false;
        this.showErrorFile = false;
        this.file = null;
      },
      toggleAddSalesModal() {
        const body = document.querySelector('body');
        this.activeAddSalesModal = !this.activeAddSalesModal;
        if (this.activeAddSalesModal) {
          body.classList.add('modal-open');
          this.initForm();
        } else {
          body.classList.remove('modal-open');
        }
      },
      toggleAddFileModal() {
        const body = document.querySelector('body');
        this.activeAddFileModal = !this.activeAddFileModal;
        if (this.activeAddFileModal) {
          body.classList.add('modal-open');
          this.initForm();
        } else {
          body.classList.remove('modal-open');
        }
      },
      calculateIncentive() {
        const path = this.backendHost+`/calculate-incentives`;
        axios.post(path, this.sales)
          .then((res) => {
            this.message = 'Calculate';
            this.activeCalculation = true;
            this.commission_sp = [];
            this.commission_sm = [];
            this.commission_gm = [];

            this.mapResponseCalculation(this.commission_sp, res.data.data.SP)
            this.mapResponseCalculation(this.commission_sm, res.data.data.SM)
            this.mapResponseCalculation(this.commission_gm, res.data.data.GM)
            
          })
          .catch((error) => {
            console.error(error);
          });
      },
      mapResponseCalculation(model, data) {
        Object.values(data).forEach(c => {
                var value = {
                    name: c.name,
                    total_sales_point: c.total_sales_point,
                    commission_point: c.commission_point,
                    performance_incentive: this.formatRupiah(c.performance_incentive),
                    total_active_sp: c.list_active_sp.length,
                    total_active_sm: c.list_active_sm.length,
                    red_total_item: "",
                    red_total_sales_point: "",
                    red_commission_point: "",
                    red_basic_commission: "",
                    blue_total_item: "",
                    blue_total_sales_point: "",
                    blue_commission_point: "",
                    blue_basic_commission: "",
                    yellow_total_item: "",
                    yellow_total_sales_point: "",
                    yellow_commission_point: "",
                    yellow_basic_commission: "",

                };
                var basic_commission = 0;
                Object.values(c.commissions).forEach(c => {
                    basic_commission += c.basic_commission
                });
                if(c.commissions.red){
                    value["red_total_item"] = c.commissions.red.total_item;
                    value["red_total_sales_point"] = c.commissions.red.total_sales_point;
                    value["red_commission_point"] = c.commissions.red.commission_point;
                    value["red_basic_commission"] = this.formatRupiah(c.commissions.red.basic_commission);
                }
                if(c.commissions.blue){
                    value["blue_total_item"] = c.commissions.blue.total_item;
                    value["blue_total_sales_point"] = c.commissions.blue.total_sales_point;
                    value["blue_commission_point"] = c.commissions.blue.commission_point;
                    value["blue_basic_commission"] = this.formatRupiah(c.commissions.blue.basic_commission);
                }
                if(c.commissions.yellow){
                    value["yellow_total_item"] = c.commissions.yellow.total_item;
                    value["yellow_total_sales_point"] = c.commissions.yellow.total_sales_point;
                    value["yellow_commission_point"] = c.commissions.yellow.commission_point;
                    value["yellow_basic_commission"] = this.formatRupiah(c.commissions.yellow.basic_commission);
                }
                
                value["basic_commission"] = this.formatRupiah(basic_commission);
                value["total_commission"] = this.formatRupiah(basic_commission + c.performance_incentive)
                model.push(value)
            });
      },
      formatRupiah(number){
        return new Intl.NumberFormat("id-ID", {
            style: "currency",
            currency: "IDR",
            minimumFractionDigits: 0,
        })
            .format(number)
            .replace("IDR", "Rp") + ',-';
        }
    },
  };
  </script>