Summary:	Unicode character map
Summary(pl):	Mapa znaków unikodowych
Name:		gucharmap
Version:	0.8.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	bef018936d47019990fe84ce7e8e23bc
Patch0:		%{name}-destdir.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.2.1
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gucharmap is a featureful unicode character map.

%description -l pl
Gucharmap jest warto¶ciow± map± znaków unikodowych.

%package devel
Summary:	Headers for gucharmap
Summary(pl):	Pliki nag³ówkowe gucharmap
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2-devel >= 2.2.0
Requires:	libgnomeui-devel >= 2.3.3.1-2
Requires:	pango-devel >= 1.2.1

%description devel
The gucharmap-devel package includes the header files that you will
need to use gucharmap.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji programów
u¿ywaj±cych gucharmap.

%package static
Summary:	Static gucharmap libraries
Summary(pl):	Statyczne biblioteki gucharmap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of gucharmap libraries.

%description static -l pl
Statyczna wersja bibliotek gucharmap.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-gtk-immodules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf gucharmap $RPM_BUILD_ROOT%{_bindir}/charmap

# remove useless files
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.2.0/immodules/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/ldconfig
gtk-query-immodules-2.0 >/etc/gtk-2.0/gtk.immodules

%postun
umask 022
/sbin/ldconfig
gtk-query-immodules-2.0 >/etc/gtk-2.0/gtk.immodules

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*charmap
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/2.2.0/immodules/im-gucharmap.so
%{_desktopdir}/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
