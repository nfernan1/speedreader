SPOT_RADIUS_FRAC = 0.07



class Spot:
    def __init__(self, center: coordinate.Coordinate, radius_frac: float):
        '''
        Initialize a newly-created Spot object, given its center
        coordinate (a Coordinate object) and the spot's radius (in
        fractional coordinates).
        '''
        self._center = center
        self._radius_frac = radius_frac


    def center_coordinate(self) -> coordinate.Coordinate:
        '''
        Returns a Coordinate object representing this Spot's
        center coordinate.
        '''
        return self._center


    def radius_frac(self):
        '''
        Returns the radius of this Spot, in terms of fractional
        coordinates.
        '''
        return self._radius_frac


    def contains(self, coordinate: coordinate.Coordinate) -> bool:
        '''
        Returns True if the given Coordinate object lies within
        this Spot, False otherwise.
        '''

        # Since Coordinate objects know how to calculate a distance
        # between themselves and other Coordinate objects, all we
        # need to do is ask the center coordinate how far it is
        # from the given coordinate; if that's less than or equal
        # to the radius, the given coordinate is within the spot.
        return self._center.frac_distance_from(coordinate) <= self._radius_frac
######################################################################
    
  def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        # When the canvas is clicked, tkinter generates an event.  Since
        # we've bound to this method to that event, this method will be
        # called whenever the canvas is clicked.  The event object passed
        # to this method will have two useful attributes:
        #
        # * event.x, which specifies the x-coordinate where the click
        #   occurred
        # * event.y, which specifies the y-coordinate where the click
        #   occurred
        #
        # tkinter is not aware of the concept of fractional coordinates.
        # It always returns absolute coordinates.  But that's okay,
        # because we can simply create a Coordinate object and let it
        # do the appropriate conversion for us.
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        click_coordinate = coordinate.from_absolute(
            (event.x, event.y), (width, height))

        # Ask the SpotsState object to handle the click, by either
        # adding or removing a spot.
        self._state.handle_click(click_coordinate)

        # Now that a spot has either been added or removed, redraw
        # the dots.
        self._redraw_all_spots()
        

    def _redraw_all_spots(self) -> None:
        # Delete and redraw all of the spots.  Since spots are represented
        # by Spot objects that contain a top-left and bottom-right
        # Coordinate object, we can simply ask these Coordinate objects
        # to return their absolute coordinate and use that to do the
        # drawing.
        self._canvas.delete(tkinter.ALL)

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        for spot in self._state.all_spots():
            center_x, center_y = spot.center_coordinate().absolute(
                (canvas_width, canvas_height))

            radius_x = spot.radius_frac() * canvas_width
            radius_y = spot.radius_frac() * canvas_height
            
            self._canvas.create_oval(
                center_x - radius_x, center_y - radius_y,
                center_x + radius_x, center_y + radius_y,
                fill = '#ffff00', outline = '#000000')
