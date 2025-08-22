"""
Centroid Addition

This module contains functions for adding centroids of overlapping stars of known 
position and flux to find their cumulative centroid.
"""

import numpy as np
import pandas as pd

class CentroidAddition:

    @staticmethod
    def add_centroids(positions: np.ndarray, fluxes: np.ndarray) -> np.ndarray:
        """
        Add centroids of overlapping stars.

        Parameters:
        positions (np.ndarray): Array of shape (N, 2) where N is the number of stars,
                                and each row contains the (x, y) aparent position of 
                                a magnifiedstar.
        fluxes (np.ndarray): Array of shape (N,) containing the flux of each star.

        Returns:
        np.ndarray: The cumulative centroid position as an array [x, y].
        """
        if len(positions) != len(fluxes):
            raise ValueError("Positions and fluxes must have the same length.")

        total_flux = np.sum(fluxes)
        if total_flux == 0:
            return np.array([0.0, 0.0])

        weighted_positions = positions.T * fluxes
        cumulative_centroid = np.sum(weighted_positions, axis=1) / total_flux

        return cumulative_centroid

    def simulate_astrometric_shift(
            self, 
            light_curve_df: pd.DataFrame, 
            source_position: np.ndarray, 
            lens_positions: np.ndarray, 
            lens_fluxes: np.ndarray
        ) -> pd.DataFrame:
        """
        Simulate astrometric shifts in a light curve due to lensing.

        Note:
        ----
        The blend flux is assumed to be zero for simplicity.

        Parameters:
        ----------
        light_curve_df (pd.DataFrame): DataFrame containing the light curve data with 
                                       a 'relative_flux' column.
        source_position (np.ndarray): Array of shape (2,) containing the (x, y) aparent
                                      position of the magnified source star.
        lens_positions (np.ndarray): Array of shape (N, 2) where N is the number of lenses,
                                     and each row contains the (x, y) position of a lens.
        lens_fluxes (np.ndarray): Array of shape (N,) containing the relative flux of each 
                                  lens.

        Returns:
        -------
        pd.DataFrame: The input DataFrame with an additional 'astrometric_shift' column.
        """
        shifts = []
        for _, row in light_curve_df.iterrows():
            relative_flux = row['relative_flux']
            if relative_flux <= 0:
                shifts.append(np.array([0.0, 0.0]))
                continue

            # Calculate the effective flux of the source
            magnified_source_flux = relative_flux

            # Combine source and lens positions and fluxes
            all_positions = np.vstack([source_position, lens_positions])
            all_fluxes = np.hstack([magnified_source_flux, lens_fluxes])

            # Calculate cumulative centroid
            cumulative_centroid = self.add_centroids(all_positions, all_fluxes)
            
            # Calculate shift from original source position
            shift = cumulative_centroid - source_position
            shifts.append(shift)
        
        light_curve_df['astrometric_shift_x'] = [shift[0] for shift in shifts]
        light_curve_df['astrometric_shift_y'] = [shift[1] for shift in shifts]

        return light_curve_df
    
    def plot_astrometric_shifts(
            self, 
            light_curve_df: pd.DataFrame, 
            t_ref: float, 
            theta_E: float, 
            mu_rel: float):
        """
        Plot astrometric shifts from the light curve DataFrame with heat maps of 
        the PSFs and the astrometric shifts.

        Parameters:
        ----------
        light_curve_df (pd.DataFrame): DataFrame containing the light curve data with an 'astrometric_shift' column.
        t_ref (float): reference time of the lensing event in simulation time.
        theta_E (float): Einstein radius in arcseconds.
        mu_rel (float): Relative proper motion in arcseconds per year in ecliptic North and East directions.
        """
        import matplotlib.pyplot as plt

        psf_width = 0.1
        pixel_scale = 0.05

        # create an 30x30 image array
        psf_image = np.zeros((30, 30))

        # Get the rotation angle from mu_rel
        angle = np.arctan2(mu_rel[1], mu_rel[0])

        # Interpolate (linearly) the astrometric shift at time t0 (which may not be an exact epoch)
        times = light_curve_df['Simulation_time'].to_numpy()
        shift_x_vals = light_curve_df['astrometric_shift_x'].to_numpy()
        shift_y_vals = light_curve_df['astrometric_shift_y'].to_numpy()

        # Linear interpolation (no extrapolation beyond range; clamp to edges)
        shift_x_tref = np.interp(t_ref, times, shift_x_vals)
        shift_y_tref = np.interp(t_ref, times, shift_y_vals)

        # Lens positions (lens1_x lens1_y lens2_x lens2_y)
        lens_positions = np.array([
            light_curve_df['lens1_x'].to_numpy(), light_curve_df['lens1_y'].to_numpy(),
            light_curve_df['lens2_x'].to_numpy(), light_curve_df['lens2_y'].to_numpy()
        ])
        lens_positions_tref = [np.interp(t_ref, times, lens_positions[i]) for i in range(lens_positions.shape[0])]

        # Source position (source_x source_y)
        source_position = np.array([
            light_curve_df['source_x'].to_numpy(),
            light_curve_df['source_y'].to_numpy()
        ])
        source_position_tref = [np.interp(t_ref, times, source_position[i]) for i in range(source_position.shape[0])]
        magnified_source_tref = np.array([
            light_curve_df['measured_relative_flux'].to_numpy()
        ])
        magnified_source_tref = np.interp(t_ref, times, magnified_source_tref)

        # scale theta_E (mas) to pixel scale 
        x_pixel_positions_mas = np.arange(-15, 15) * pixel_scale 
        y_pixel_positions_mas = np.arange(-15, 15) * pixel_scale


        shifts = np.array(light_curve_df['astrometric_shift'].tolist())
        plt.figure(figsize=(10, 6))
        plt.quiver(light_curve_df.index, np.zeros_like(shifts[:, 0]), shifts[:, 0], shifts[:, 1],
                   angles='xy', scale_units='xy', scale=1, color='blue')
        plt.title('Astrometric Shifts')
        plt.xlabel('Time (arbitrary units)')
        plt.ylabel('Shift (arcseconds)')
        plt.grid()
        plt.show()