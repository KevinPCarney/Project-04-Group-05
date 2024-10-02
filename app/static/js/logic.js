$(document).ready(function() {
  console.log("Page Loaded");

  $("#filter").click(function() {
      // alert("button clicked!");
      makePredictions();
  });
});


// call Flask API endpoint
function makePredictions() {
  var Weather = $("#Weather").val();
  var Roadway_Type = $("#Roadway_Type").val();
  var Model_Year = $("#Model_Year").val();
  var Passengers_Belted = $("#Passengers_Belted").val();
  var Time_of_Day = $("#Time_of_Day").val();
  var Speed_Limit = $("#Speed_Limit").val();
  var Roadway_Surface = $("#Roadway_Surface").val();

  // check if inputs are valid

  // create the payload
  var payload = {
      "Weather": Weather,
      "Roadway_Type": Roadway_Type,
      "Model_Year": Model_Year,
      "Passengers_Belted": Passengers_Belted,
      "Time_of_Day": Time_of_Day,
      "Speed_Limit": Speed_Limit,
      "Roadway_Surface": Roadway_Surface,
   }

  // Perform a POST request to the query URL
  $.ajax({
      type: "POST",
      url: "/makePredictions",
      contentType: 'application/json;charset=UTF-8',
      data: JSON.stringify({ "data": payload }),
      success: function(returnedData) {
          // print it
          console.log(returnedData);
          let pred = returnedData["prediction"]

          if (pred["car_crash_pred"] === "high_risk") {
              $("#output").text(`This is your probability of a car crash ${(pred["prob_high_risk"]*100).toFixed(2)}%.`);
          } else {
              $("#output").text(`Congratulations! This is your probability of a car crash ${(pred["prob_high_risk"]*100).toFixed(2)}%.`);
          }

      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
          alert("Status: " + textStatus);
          alert("Error: " + errorThrown);
        }
    });

    }
